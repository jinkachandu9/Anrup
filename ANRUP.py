from stockValues import getStock
from updateGoogleSheet import update_cell, update_cell_batch 
from sentiment import read_sheet
from datetime import datetime
import requests,webbrowser
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
from googleSearch import googleOnlySearch
import time
import json
import threading

# x = [2]
# index1=2
# sheet_id = "1PB7fOtHfhssJVvj_5BaJGQX-X3hSAu2O3jOrHo920r8"

# def update_only_required(index1,google_shee,sheet_name,script_code):
#     resultList = []
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     resultList.append(current_time)
#     update_cell(sheet_id,sheet_name,resultList,"A"+str(index1))
#     update_cell(sheet_id,sheet_name,resultList,"C"+str(index1))
#     temp = []
#     temp.append(googleOnlySearch(google_shee))
#     update_cell(sheet_id,sheet_name,temp,"B"+str(index1))
#     temp = []
#     temp.append(getStock(script_code))
#     update_cell(sheet_id,sheet_name,temp,"D"+str(index1))
  

# def run(condition,x):
#     index1=x[0]
#     try:
#         while condition == True:


#             #reliance
#             google_shee="https://www.google.com/search?q=good+news+for+Reliance+Industries+Limited+(RIL)&rlz=1C1VDKB_enIN1037IN1037&sxsrf=AJOqlzVakrUx5LqwmLaQT0EL92OUoc9uDQ:1675700753525&source=lnt&tbs=qdr:h&sa=X&ved=2ahUKEwj9pafhp4H9AhWvrlYBHTA4A44QpwV6BAgCEBY&biw=1920&bih=969&dpr=1"
#             sheet_name= "RIL!"
#             script_code='500325'

#             update_only_required(index1,google_shee,sheet_name,script_code)

#             #TCS
#             google_shee="https://www.google.com/search?q=good+news+for+Tata+Consultancy+Services+%28TCS%29&rlz=1C1VDKB_enIN1037IN1037&biw=1920&bih=969&tbs=qdr%3Ah&sxsrf=AJOqlzXejFk798MPvwAj3xmQ6wmMRWahPg%3A1675700760066&ei=GCrhY8LVA63l2roP59OcKA&ved=0ahUKEwjCwbbkp4H9AhWtslYBHecpBwUQ4dUDCA8&uact=5&oq=good+news+for+Tata+Consultancy+Services+%28TCS%29&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAEyBQghEKABOgoIABBHENYEELADSgQIQRgASgQIRhgAULsBWLsBYNoEaAFwAXgAgAHCAYgBwgGSAQMwLjGYAQCgAQKgAQHIAQXAAQE&sclient=gws-wiz-serp"
#             sheet_name= "TCS!"
#             script_code='532540'
#             update_only_required(index1,google_shee,sheet_name,script_code)

#             #HDFC
#             google_shee="https://www.google.com/search?q=good+news+for+Housing+Development+Finance+Corporation+%28HDFC%29&rlz=1C1VDKB_enIN1037IN1037&biw=1920&bih=969&tbs=qdr%3Ah&sxsrf=AJOqlzVYqUpix2DU6paR5VaTuIkP4ni3SQ%3A1675701018367&ei=GivhY66RFsbj2roPpLU7&ved=0ahUKEwiuhszfqIH9AhXGsVYBHaTaDgAQ4dUDCA8&uact=5&oq=good+news+for+Housing+Development+Finance+Corporation+%28HDFC%29&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAEyBQghEKABOgoIABBHENYEELADSgQIQRgASgQIRhgAUKIOWKIOYKAUaANwAXgAgAHZAYgB2QGSAQMyLTGYAQCgAQKgAQHIAQjAAQE&sclient=gws-wiz-serp"
#             sheet_name= "HDFC!"
#             script_code='500010'
#             update_only_required(index1,google_shee,sheet_name,script_code)

#             #Infosys Limited
#             google_shee="https://www.google.com/search?q=good+news+for+Infosys+Limited&rlz=1C1VDKB_enIN1037IN1037&biw=1920&bih=969&tbs=qdr%3Ah&sxsrf=AJOqlzUiSykcEDkad-6DeBPuS6GyclAsMw%3A1675701205292&ei=1SvhY_e_EZGx2roPqOSE2AI&ved=0ahUKEwi3_ty4qYH9AhWRmFYBHSgyASsQ4dUDCA8&uact=5&oq=good+news+for+Infosys+Limited&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAEyCAghEBYQHhAdOgoIABBHENYEELADSgQIQRgASgQIRhgAUMqABljKgAZgtYgGaANwAXgAgAGJAogBiQKSAQMyLTGYAQCgAQKgAQHIAQjAAQE&sclient=gws-wiz-serp"
#             sheet_name= "Infosys Limited!"
#             script_code='500209'
#             update_only_required(index1,google_shee,sheet_name,script_code)
            
#             #HDFC Bank Limited
#             google_shee="https://www.google.com/search?q=good+news+for+HDFC+Bank+Limited&rlz=1C1VDKB_enIN1037IN1037&biw=1920&bih=969&tbs=qdr%3Ah&sxsrf=AJOqlzXLgX8Zlgvc3FnCGyrtlG9Ud7nppg%3A1675701306561&ei=OizhY-bwIa_c2roP_620IA&ved=0ahUKEwjm9YHpqYH9AhUvrlYBHf8WDQQQ4dUDCA8&uact=5&oq=good+news+for+HDFC+Bank+Limited&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIICCEQFhAeEB0yCwghEBYQHhDxBBAdMggIIRAWEB4QHUoECEEYAEoECEYYAFAAWABgtgloAHABeACAAdYBiAHWAZIBAzItMZgBAKABAqABAcABAQ&sclient=gws-wiz-serp"
#             sheet_name= "HDFC Bank Limited!"
#             script_code= '500180'
#             update_only_required(index1,google_shee,sheet_name,script_code)

#             #Bharat Petroleum Corporation Limited (BPCL)
#             google_shee="https://www.google.com/search?q=good+news+for+Bharat+Petroleum+Corporation+Limited+%28BPCL%29&rlz=1C1VDKB_enIN1037IN1037&biw=1920&bih=969&tbs=qdr%3Ah&sxsrf=AJOqlzVITTUNycfbUROZcYoiBnahtIlRng%3A1675701765483&ei=BS7hY6qRHezC4-EPwO2LiAc&ved=0ahUKEwjqp-zDq4H9AhVs4TgGHcD2AnEQ4dUDCA8&uact=5&oq=good+news+for+Bharat+Petroleum+Corporation+Limited+%28BPCL%29&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEMgcIABAeEKIEMgUIABCiBDoKCAAQRxDWBBCwA0oECEEYAEoECEYYAFCUAliUAmDrBmgBcAF4AIABgAKIAYACkgEDMi0xmAEAoAECoAEByAEIwAEB&sclient=gws-wiz-serp"
#             sheet_name= "BPCL!"
#             script_code= '500547'
#             update_only_required(index1,google_shee,sheet_name,script_code)

#             #Hindustan Petroleum Corporation Limited (HPCL)
#             google_shee="https://www.google.com/search?q=good+news+for+Hindustan+Petroleum+Corporation+Limited+%28HPCL%29&rlz=1C1VDKB_enIN1037IN1037&biw=1920&bih=969&tbs=qdr%3Ah&sxsrf=AJOqlzW0D7k2F-VxywWewpB0RMYy4Kte1Q%3A1675701993661&ei=6S7hY8iCKL7N2roP9qGE4A8&ved=0ahUKEwiIm9OwrIH9AhW-plYBHfYQAfwQ4dUDCA8&uact=5&oq=good+news+for+Hindustan+Petroleum+Corporation+Limited+%28HPCL%29&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwA0oECEEYAEoECEYYAFCvAVivAWDXBGgBcAF4AIABAIgBAJIBAJgBAKABAqABAcgBCMABAQ&sclient=gws-wiz-serp"
#             sheet_name= "HPCL!"
#             script_code= '500104'
#             update_only_required(index1,google_shee,sheet_name,script_code)

#             #ITC Limited
#             google_shee="https://www.google.com/search?q=good+news+for+ITC+Limited&rlz=1C1VDKB_enIN1037IN1037&biw=1920&bih=969&tbs=qdr%3Ah&sxsrf=AJOqlzUWjCRQYpODfFEfJUeGf0gcLRPpIg%3A1675702005885&ei=9S7hY8rTNeqB2roPyZC8KA&ved=0ahUKEwiKor22rIH9AhXqgFYBHUkIDwUQ4dUDCA8&uact=5&oq=good+news+for+ITC+Limited&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJ0oECEEYAEoECEYYAFAAWABgrARoAHABeACAAaYBiAGmAZIBAzAuMZgBAKABAqABAcABAQ&sclient=gws-wiz-serp"
#             sheet_name= "ITC Limited!"
#             script_code= '500875 '
#             update_only_required(index1,google_shee,sheet_name,script_code)

#             #Kotak Mahindra Bank Limited
#             google_shee="https://www.google.com/search?q=good+news+for+Kotak+Mahindra+Bank+Limited&rlz=1C1VDKB_enIN1037IN1037&biw=1920&bih=969&tbs=qdr%3Ah&sxsrf=AJOqlzW0D7k2F-VxywWewpB0RMYy4Kte1Q%3A1675701993661&ei=6S7hY8iCKL7N2roP9qGE4A8&ved=0ahUKEwiIm9OwrIH9AhW-plYBHfYQAfwQ4dUDCA8&uact=5&oq=good+news+for+Kotak+Mahindra+Bank+Limited&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIICCEQFhAeEB0yCAghEBYQHhAdOgoIABBHENYEELADSgQIQRgASgQIRhgAUOTcAljk3AJgvd8CaAFwAXgAgAHFAYgBxQGSAQMwLjGYAQCgAQKgAQHIAQjAAQE&sclient=gws-wiz-serp"
#             sheet_name= "Kotak Mahindra Bank Limited!"
#             script_code= '500247' 
#             update_only_required(index1,google_shee,sheet_name,script_code)

#             #Bajaj Finserv Limited
#             google_shee="https://www.google.com/search?q=good+news+for+Bajaj+Finserv+Limited&rlz=1C1VDKB_enIN1037IN1037&biw=1920&bih=969&tbs=qdr%3Ah&sxsrf=AJOqlzV9EUFZIxpX-6-x58m_LSmpU8QsAA%3A1675702124141&ei=bC_hY4aoCLaG2roPr-SUKA&ved=0ahUKEwiGju_urIH9AhU2g1YBHS8yBQUQ4dUDCA8&uact=5&oq=good+news+for+Bajaj+Finserv+Limited&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIICCEQFhAeEB0yCAghEBYQHhAdMggIIRAWEB4QHUoECEEYAEoECEYYAFAAWABg-ApoAHABeACAAdIBiAHSAZIBAzItMZgBAKABAqABAcABAQ&sclient=gws-wiz-serp"
#             sheet_name= "Bajaj Finserv Limited!"
#             script_code= '532978' 
#             update_only_required(index1,google_shee,sheet_name,script_code)

#             time.sleep(60 * 1)
#             index1=index1+1
#             x[0]=index1
#     except:
#         print("failed")   
# run(True,x)  
# with open('BigData.json') as json_file:

#     data1 = json.load(json_file)



# def update_only_required(index1,google_shee,sheet_name,script_code):
#     resultList = []
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     resultList.append(current_time)
 #   update_cell(sheet_id,sheet_name,resultList,"A"+str(index1))
#     update_cell(sheet_id,sheet_name,resultList,"C"+str(index1))
#     temp = []
#     temp.append(googleOnlySearch(google_shee))
#     update_cell(sheet_id,sheet_name,temp,"B"+str(index1))
#     temp = []
#     temp.append(getStock(script_code))
#     update_cell(sheet_id,sheet_name,temp,"D"+str(index1))

# x = [2]
# def updateExcelSheet(x):
#     index1=x[0]
#     f = open('BigData.json')
#     datas = json.load(f)
#     datas= datas[:100]

#     try:
#         while (True):
#             for data in datas:
#                 try:
#                   update_only_required(index1,data["google_link"],data["sheet_name"]+"!",data["script_code"])
#                 except Exception as e:
#                   print(f"failed:{e}")  
#             index1=index1+1
#             x[0]=index1
#     except Exception as e:
#         print("failed:{e}")  
#     f.close() 
# while(True):
#     updateExcelSheet(x)

# def update_excel_sheet(x):
#     index1 = x[0]
#     f = open('BigData.json')
#     datas = json.load(f)
#     datas = datas[:10]
#     while(True):
#         update_data = []
#         for data in datas:
#             try:
#                 result_list = []
#                 now = datetime.now()
#                 current_time = now.strftime("%H:%M:%S")
#                 result_list.append(current_time)
#                 google_search_resultList=[]
#                 google_search_result = googleOnlySearch(data["google_link"])
#                 google_search_resultList.append(google_search_result)
#                 stock_info_list=[]
#                 stock_info = getStock(data["script_code"])
#                 stock_info_list.append(stock_info)
#                 update_data.append([index1,data["sheet_name"],result_list, google_search_resultList, result_list, stock_info_list,data["google_link"]])
#             except Exception as e:
#                 print(f"Failed: {e}")
            
#     # Update all cells at once using batch processing
#         update_cell_batch( update_data)
        
#         index1 = index1+1
#     x[0] = index1
#     f.close()
# x = [2]
# update_excel_sheet(x)
# import threading

# def update_only_required(index1, google_shee, sheet_name, script_code):
#     resultList = []
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     resultList.append(current_time)
#     update_cell(sheet_id, sheet_name, resultList, "A" + str(index1))
#     update_cell(sheet_id, sheet_name, resultList, "C" + str(index1))
#     temp = []
#     temp.append(googleOnlySearch(google_shee))
#     update_cell(sheet_id, sheet_name, temp, "B" + str(index1))
#     temp = []
#     temp.append(getStock(script_code))
#     update_cell(sheet_id, sheet_name, temp, "D" + str(index1))

# def updateExcelSheetThread(data, index1):
#     sheetName = data["sheet_name"]
#     sheetName = sheetName.replace(' ', "%")
#     temp = "https://www.google.co.in/search?q=" + "good%news%for%" + sheetName + "&tbs=qdr:h"
#     try:
#         update_only_required(index1, temp, data["sheet_name"] + "!", data["script_code"])
#     except Exception as e:
#         print(f"failed:{e}")


# def updateExcelSheet(x):
#     index1 = x[0]
#     f = open('BigData.json')
#     datas = json.load(f)
#     datas= datas[:50]
#     try:
#         while (True):
#             threads = []
#             for data in datas:
#                 while len(threads) >= 20:
#                     for t in threads:
#                         if not t.is_alive():
#                             threads.remove(t)
#                 t = threading.Thread(target=updateExcelSheetThread, args=(data, index1))
#                 t.start()
#                 threads.append(t)

#             for t in threads:
#                 t.join()

#             index1 = index1 + 1
#             x[0] = index1
#     except Exception as e:
#         print("failed:{e}")
#     f.close()






# from multiprocessing import Process, Manager

# def updateExcelSheet(index1, q):
#     f = open('BigData.json')
#     datas = json.load(f)
#     try:
#         while (True):
#             for data in datas:
#                 sheetName=data["sheet_name"]
#                 sheetName=sheetName.replace(' ', "%")
#                 temp="https://www.google.co.in/search?q="+"good%news%for%"+sheetName+"&tbs=qdr:h"
#                 try:
#                   update_only_required(index1,temp,data["sheet_name"]+"!",data["script_code"])
#                 except Exception as e:
#                   print(f"failed:{e}")  
#             index1=index1+1
#             q.put(index1)
#     except Exception as e:
#         print("failed:{e}")  
#     f.close() 

# if __name__ == '__main__':
#     manager = Manager()
#     q = manager.Queue()
#     q.put(2)
#     processes = []
#     for i in range(4):
#         p = Process(target=updateExcelSheet, args=(q.get(), q))
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()

  
# Iterating through the json
# list

  
# Closing file

import json
from datetime import datetime

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def process_data(data, index):
    try:
        now = datetime.now().strftime("%H:%M:%S")
        google_search_result = googleOnlySearch(data["google_link"])
        stock_info = getStock(data["script_code"])
        return [index, data["sheet_name"], [now], [google_search_result], now, [stock_info], data["google_link"]]
    except Exception as e:
        print(f"Failed: {e}")

def run_parallel(datas, index1):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_data, datas, [index1]*len(datas)))
    return [result for result in results if result is not None]






def update_excel_sheet(x):
    index1 = x[0]
    f = open('BigData.json')
    datas = json.load(f)
    datas = datas[:10]
    while(True):
        update_data = []
        try:
            update_data = run_parallel(datas, index1)
    # Update all cells at once using batch processing
            print("working")
            update_cell_batch( update_data)
            index1 = index1+1
        except:
            print("ex")        
        
    x[0] = index1
    f.close()
x = [2]
while(True):
 update_excel_sheet(x)
