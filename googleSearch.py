from updateGoogleSheet import update_cell
from sentiment import read_sheet
from datetime import datetime
import requests,webbrowser
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
from playsound import playsound
from datetime import datetime


#update_row(sheet_id,resultList,"Sheet2!B1:B10")
index1 = 1
def googleSearch(searchQuery,index1):
    google_search = requests.get(searchQuery)
    soup =BeautifulSoup(google_search.text,'html.parser')
    results = soup.find_all("h3")
    resultList = []
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    resultList.append(current_time)
    for result in results:
        header = result.text
        resultList.append(header)
    sheet_id = "1PB7fOtHfhssJVvj_5BaJGQX-X3hSAu2O3jOrHo920r8"
    update_cell(sheet_id,resultList,"A"+str(index1))
    index1=index1+1
    sentimentalList = []
    sentimentalList.append("")
    for result in resultList:
        sentimentalList.append(read_sheet(result))
    update_cell(sheet_id,sentimentalList,"A"+str(index1))
    index1=index1+1

sheet_id = "1PB7fOtHfhssJVvj_5BaJGQX-X3hSAu2O3jOrHo920r8"
def update_only_required():
    resultList = []
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    resultList.append(current_time)
    update_cell(sheet_id,resultList,"A1")
# sleep(60*1)  # Wait for 15 minutesrun(1,index1)
def run(condition,index1):
    while condition == True:
        update_only_required()
import requests
def googleOnlySearch(searchQuery):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    url = searchQuery
    response = requests.get(url, headers=headers)
    soup =BeautifulSoup(response.text,'html.parser')
    results = soup.find_all("h3")
    resultList = set()
    for result in results:
        header = result.text
        resultList.add(header)
    sentimentalList = set()
    sentimentalResult = 0
    for result in resultList:
        sentimentalList.add(read_sheet(result))
        sentimentalResult = sentimentalResult + read_sheet(result)
    return sentimentalResult
def google_search1(query):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url, headers=headers)
    soup =BeautifulSoup(response.text,'html.parser')
    results = soup.find_all("h3")
    resultList = set()
    print(results)
    return response.text

#search_results = google_search1("reliance industries ltd")
#print(search_results)

# def oldgoogleOnlySearch(searchQuery):
#     google_search = requests.get(searchQuery)
#     soup =BeautifulSoup(google_search.text,'html.parser')
#     results = soup.find_all("h3")
#     resultList = set()
#     print(results)
#     print("-------------------------------------------------------------")
#     for result in results:
#         header = result.text
#         resultList.add(header)
#     sentimentalList = set()
#     sentimentalResult = 0
#     print(resultList)
#     for result in resultList:
#         sentimentalList.add(read_sheet(result))
#         print(result,read_sheet(result))
#         sentimentalResult = sentimentalResult + read_sheet(result)
#     return sentimentalResult
#googleOnlySearch("searchQuery")
def getStockPrice():
    searchQuery = "https://www.google.com/search?q=stock+price+of+for+lti+mindtree&rlz=1C1VDKB_enIN1037IN1037&oq=stock+price+of+for+lti+mindtree&aqs=chrome..69i57j0i546l3.9321j0j7&sourceid=chrome&ie=UTF-8"
    google_search = requests.get(searchQuery)
    soup =BeautifulSoup(google_search.text,'html.parser')
    lti_price = soup.find('div', {'data-attrid': 'Price'}).find('span', {'jsname': 'vWLAgc'})

    # Find the stock price of Mindtree
    mindtree_price = soup.find('div', {'data-attrid': 'Price'}).find('span', {'jsname': 'vWLAgc'})

    print("L&T Infotech stock price:", lti_price)
    print("Mindtree stock price:", mindtree_price)
    
def googleStockPrice(searchQuery):
    google_search = requests.get(searchQuery)
    soup =BeautifulSoup(google_search.text,'html.parser')
    span = soup.find('span', {'class': 'IsqQVc NprOob wT3VGc'})
    print(span)
    span = soup.find('span', {'jsname': 'vWLAgc'})
    print(span)
#googleStockPrice("https://www.google.com/search?q=share+price+of+infosys&rlz=1C1VDKB_enIN1037IN1037&sxsrf=AJOqlzU3IOHxugLd0nL320Ive_eJ_YorEQ%3A1675758331947&ei=-wriY-S6Of3gseMPnfih-Aw&oq=share+price+of+&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgwIIxAnEJ0CEEYQ-gEyBAgjECcyBAgjECcyBAgAEEMyCwgAEIAEELEDEIMBMggIABCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMggIABCxAxCDATILCAAQgAQQsQMQgwE6CggAEEcQ1gQQsAM6BwgAELADEEM6CggAELEDEIMBEEM6BQgAEIAEOgYIABAWEB46BQgAEIYDSgQIQRgASgQIRhgAUJIBWKcLYJ08aAJwAXgAgAGDBYgBiRKSAQgwLjE0LjUtMZgBAKABAcgBCsABAQ&sclient=gws-wiz-serp")
#getStockPrice()