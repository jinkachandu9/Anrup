from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import sentiment



# def read_sheet(sheet_id, range_name):
#     credentials = Credentials.from_service_account_file("aqueous-coder-323617-6de30a1c46e4.json")
#     service = build("sheets", "v4", credentials=credentials)
#     result = service.spreadsheets().values().get(
#         spreadsheetId=sheet_id, range=range_name).execute()
#     values = result.get("values", [])
#     if not values:
#         print("No data found.")
#     else:
#         print("Data:")
#         for row in values:
#             print(row)

def clear_column_H(sheet_id, range_name):
    credentials = Credentials.from_service_account_file("aqueous-coder-323617-6de30a1c46e4.json")
    service = build("sheets", "v4", credentials=credentials)
    clear_request_body = {"ranges": [range_name], "sheetId": sheet_id}
    result = service.spreadsheets().values().batchClear(
        spreadsheetId=sheet_id, body=clear_request_body).execute()
    print(f"{result.get('clearedRange')} range cleared.")



def copy_column_C_to_H(sheet_id, range_name):
    credentials = Credentials.from_service_account_file("aqueous-coder-323617-6de30a1c46e4.json")
    service = build("sheets", "v4", credentials=credentials)
    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id, range=range_name).execute()
    values = result.get("values", [])
    if not values:
        print("No data found.")
    else:
        print("Data:")
        for i, row in enumerate(values):
            if len(row) >= 4:
                values[i].append(sentiment.read_sheet(row[3]))     
    body = {"values": values}
    result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id, range=range_name,
        valueInputOption="RAW", body=body).execute()
    print(f"{result.get('updatedCells')} cells updated.")

sheet_id = "1PB7fOtHfhssJVvj_5BaJGQX-X3hSAu2O3jOrHo920r8"
range_name = "Sheet2"
#read_sheet(sheet_id, range_name)
values = [["Hello, World!"]]


range_name = "Sheet2!H2"
#clear_column_H(sheet_id, "sheet2!H:H")
#clear_column_H(sheet_id,range_name)
range_name = "Sheet2"
copy_column_C_to_H(sheet_id, range_name)