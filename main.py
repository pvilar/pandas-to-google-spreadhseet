import os
import time

import gspread
import pandas as pd
import yfinance as yf
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

# load environment
load_dotenv()

# load google credentials from env vars
GOOGLE_JSON_CREDENTIALS = os.getenv("GOOGLE_JSON_CREDENTIALS")

# variables
SPREADSHEET_NAME = 'Bitcoin_prices_last_24h'
EMAILS_LIST = [
    'pau.vilar.ribo@gmail.com'
]


def generate_google_credentials(google_credentials_dict: dict):
    """
    Populates the JSON keyfile and generates the service account credentials
    """
    # specify Google Drive and Google Sheets APIs
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    # get credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        google_credentials_dict, scopes)

    return credentials


def export_dataframe_to_google_spreadsheet(dataframe: pd.DataFrame,
                                           spreadsheet_name: str,
                                           google_credentials):
    """
    Exports a Pandas DF into a Google Spreadsheet using a Instapro service
    account and the Google Drive and Google Sheets APIs.
    """

    # authorize
    gc = gspread.authorize(google_credentials)

    # create new spreadsheet
    sh = gc.create(spreadsheet_name)

    # copy Pandas DF into the first worksheet
    worksheet = sh.sheet1
    worksheet.update([dataframe.columns.values.tolist()] +
                     dataframe.values.tolist())

    return sh


def share_spreadsheet_by_email(spreadsheet, emails_list: list):
    """
    Shares the spreadsheet to the specified email addresses
    """
    for e in emails_list:
        spreadsheet.share(e, perm_type='user', role='reader')

    return None


def main():
    print("Downloading Bitcoin prices.")
    start_time = time.time()
    df = yf.download(tickers='BTC-USD', period='24h', interval='30m')
    print("--- %s seconds ---" % (time.time() - start_time))

    print(
        "Exporting dataframe to a Google Spreadsheet and sending over email.")  # noqa E501
    google_credentials = generate_google_credentials(GOOGLE_JSON_CREDENTIALS)
    spreadsheet = export_dataframe_to_google_spreadsheet(
        dataframe=df,
        spreadsheet_name=SPREADSHEET_NAME,
        google_credentials=google_credentials)

    share_spreadsheet_by_email(spreadsheet=spreadsheet,
                               emails_list=EMAILS_LIST)
    print("Process finished.")


if __name__ == "__main__":
    main()
