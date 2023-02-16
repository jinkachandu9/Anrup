from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
def refresh_sheet(sheet_id):
    credentials = Credentials.from_service_account_file("aqueous-coder-323617-6de30a1c46e4.json")
    service = build("sheets", "v4", credentials=credentials)
    result = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
    print("Sheet refreshed.")
def update_cell(sheet_id, range_name, value):
    credentials = Credentials.from_service_account_file("aqueous-coder-323617-6de30a1c46e4.json")
    service = build("sheets", "v4", credentials=credentials)
    body = {"values": [[value]]}
    result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id, range=range_name,
        valueInputOption="RAW", body=body).execute()
    print(f"Cell {range_name} updated.")

update_cell("sheet2", "A1", "Hello World")

refresh_sheet("1PB7fOtHfhssJVvj_5BaJGQX-X3hSAu2O3jOrHo920r8")