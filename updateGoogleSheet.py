from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import json
def update_cell(sheet_id, sheet_name,value,index):
    credentials = Credentials.from_service_account_file("aqueous-coder-323617-6de30a1c46e4.json")
    service = build("sheets", "v4", credentials=credentials)
    # Define the values to be updated in the range of cells
    range_name = sheet_name+index
    values = [value]
    body = {
    "values": values
    }
    service.spreadsheets().values().update(spreadsheetId=sheet_id, range=range_name, valueInputOption="RAW", body=body).execute()
sheet_id_test = "1PB7fOtHfhssJVvj_5BaJGQX-X3hSAu2O3jOrHo920r8"
from datetime import datetime
def update_cell_batch( update_data):
    credentials = Credentials.from_service_account_file("aqueous-coder-323617-6de30a1c46e4.json")
    service = build("sheets", "v4", credentials=credentials)
    # Define the values to be updated in the range of cells
    for i in update_data:
        range_name = i[1]+'!A'+str(i[0])
        values = [[datetime.now().strftime("%H:%M:%S")]]
        body = {
        "values": values
        }
        
        service.spreadsheets().values().update(spreadsheetId=sheet_id_test, range=i[1]+'!A'+str(i[0]), valueInputOption="RAW", body=body).execute()
        service.spreadsheets().values().update(spreadsheetId=sheet_id_test, range=i[1]+'!C'+str(i[0]), valueInputOption="RAW", body=body).execute()
        values = [i[3]]
        body = {
        "values": values
        }
        service.spreadsheets().values().update(spreadsheetId=sheet_id_test, range=i[1]+'!B'+str(i[0]), valueInputOption="RAW", body=body).execute()
        values = [i[5]]
        body = {
        "values": values
        }
        service.spreadsheets().values().update(spreadsheetId=sheet_id_test, range=i[1]+'!D'+str(i[0]), valueInputOption="RAW", body=body).execute()
        



def update_with_new_tab(new_sheet_name):
    # Load the service account credentials from the JSON file
    creds = Credentials.from_service_account_file("aqueous-coder-323617-6de30a1c46e4.json")

    # Build the credentials object to access the Google Sheets API
    sheets_service = build('sheets', 'v4', credentials=creds)

    # Specify the source spreadsheet and sheet
    src_spreadsheet_id = "1PB7fOtHfhssJVvj_5BaJGQX-X3hSAu2O3jOrHo920r8"
    src_sheet_id = "1360458154"

    # Copy the sheet to a new tab in the same Google Sheet
    sheet_copy_request = {
        "destinationSpreadsheetId": src_spreadsheet_id,
    }
    result = sheets_service.spreadsheets().sheets().copyTo(spreadsheetId=src_spreadsheet_id, sheetId=src_sheet_id, body=sheet_copy_request).execute()

    # Rename the new tab to something unique
    new_sheet_id = result['sheetId']

    sheet_update_request = {
        "requests": [
            {
                "updateSheetProperties": {
                    "properties": {
                        "sheetId": new_sheet_id,
                        "title": new_sheet_name
                    },
                    "fields": "title"
                }
            }
        ]
    }
    sheets_service.spreadsheets().batchUpdate(spreadsheetId=src_spreadsheet_id, body=sheet_update_request).execute()
# f = open('BigData.json')
# datas = json.load(f)
# datas = datas[:10]
# for data in datas:
#     update_with_new_tab(data["sheet_name"])