import json


with open('reference.json', 'r') as file:
    existing_data = json.load(file)

# Loop through each object in the JSON array
for i in range(len(existing_data)):
    # Add a new key-value pair to each object
    sheetName=existing_data[i]["sheet_name"]
    sheetName=sheetName.replace(' ', "%")
    existing_data[i]['google_link'] = "https://www.google.co.in/search?q="+"good%news%for%"+sheetName+"&tbs=qdr:h"

# Write the modified JSON objects back to the file
with open('BigData.json', 'w') as file:
    json.dump(existing_data, file)




