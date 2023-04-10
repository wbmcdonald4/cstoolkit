from google.oauth2 import service_account
from googleapiclient.discovery import build

from datetime import datetime

def append_email_to_google_sheet(email):
    # Load credentials from the `credentials.json` file
    credentials = service_account.Credentials.from_service_account_file('src/secrets/credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])

    # Initialize the Google Sheets API client
    service = build('sheets', 'v4', credentials=credentials)

    # Specify the ID of your Google Sheet and the range where you want to append the data
    spreadsheet_id = '1TfPRisKLbJFWGZQMCh1Zqy3k6EIUtIoyneLvgbb8TGo'
    range_name = 'Sheet1!A:A'

    # Get the current date
    today = datetime.today().strftime('%Y-%m-%d')

    # Append the email to the specified range
    body = {
        'values': [[email, today]]
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        insertDataOption='INSERT_ROWS',
        body=body
    ).execute()

    print(f'{result.get("updates").get("updatedCells")} cells updated.')
