# Pandas to Google Spreadhseet
Python simple application for converting a Pandas DataFrame into a Google Spreadsheet and share it via email

## How to use


1. Clone the repository, create a virtual environment and install the requirements


```bash
python3 -m venv my_venv
```

```bash
source my_venv/bin/activate
```

```bash
pip install -r requirements.txt
```

2. Follow the instructions to create a service account:

https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account

3. Enable the following APIs on your Google Project from the GCP Console:
- Google Drive API
- Google Sheets API

4. Copy the `.env_dist` and rename to `.env`. Populate the credentials from the JSON file you downloaded in the step 2.

```json
GOOGLE_JSON_CREDENTIALS = '{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": ""
}'
```

5. Run the app

```bash
python3 main.py
```
