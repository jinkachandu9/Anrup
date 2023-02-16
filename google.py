from googlesearch import search

query ="https://www.google.com/search?q=good+news+for+amazon+in+last+hour&rlz=1C1VDKB_enIN1037IN1037&biw=1920&bih=969&tbs=qdr%3Ah&sxsrf=AJOqlzWiYFzggqVk9dDv3xQekNhe1EN3lw%3A1675565689782&ei=eRrfY4a3L__RseMP67uIuAQ&ved=0ahUKEwjG1_LNsP38AhX_aGwGHesdAkcQ4dUDCA8&uact=5&oq=good+news+for+amazon+in+last+hour&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAE6CggAEEcQ1gQQsANKBAhBGABKBAhGGABQnyxYnyxgvC5oAnAAeACAAa4BiAGuAZIBAzAuMZgBAKABAqABAcgBCMABAQ&sclient=gws-wiz-serp"

for i in search(query):
    print(i)