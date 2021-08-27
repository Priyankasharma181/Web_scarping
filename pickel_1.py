import requests , json
from bs4 import BeautifulSoup
from pprint import pprint
url = "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="
req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")
div1 = soup.find("div" , class_="_1EI9").span.get_text()
# print(div1)
def web_pickle():
    URL = "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    Req = requests.get(URL)
    soup_1 = BeautifulSoup(Req.text,"html.parser")
    # print(soup_1)
    main_data = soup_1.find("div",class_="_3RA-")
    pickle_name = main_data.find_all("div",class_="UGUy")
    # pprint(pickle_name)
    pickle_price = main_data.find_all("div",class_="_1kMS")
    # pprint(pickle_price)
    pickle_link = main_data.find_all("div",class_="_3nWP") 
    # pprint(pickle_link)
    link = main_data.find_all("div",class_="_3WhJ")
    # pprint(link)
    posstion = 0
    List = []
    i = 0
    while i<len(pickle_link):
        posstion += 1
        pickle_name1 = link[i].get_text()
        # pprint(pickle_name1)
        pickle_price1 = pickle_price[i].span.get_text()
        # pprint(pickle_price1)
        pickle_link1 = (link[i].a["href"])
        # pprint(pickle_link1)
        pickle_link2 = "https://paytmmall.com/"+pickle_link1
        # pprint(pickle_link2)
        dic = {"posstion":posstion,"pickle_name":pickle_name1,"pickle_price":pickle_price1,"pickle_link":pickle_link2}
        List.append(dic)
        # pprint(List)
        with open("pickle.json","w") as file:
            json.dump(List,file,indent=4)   
        i+=1
web_pickle()

