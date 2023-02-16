from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
credentials = Credentials.from_service_account_file("aqueous-coder-323617-6de30a1c46e4.json")
service = build("sheets", "v4", credentials=credentials)

sheet_id = "1PB7fOtHfhssJVvj_5BaJGQX-X3hSAu2O3jOrHo920r8"
range_name = "Sheet2!B2"
credentials = Credentials.from_service_account_file("aqueous-coder-323617-6de30a1c46e4.json")
service = build("sheets", "v4", credentials=credentials)
value = [["=IMPORTFROMGOOGLE"]]
body = {"values": value}

result = service.spreadsheets().values().update(
    spreadsheetId=sheet_id, range=range_name,
    valueInputOption="RAW", body=body).execute()