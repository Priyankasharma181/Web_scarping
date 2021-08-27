import requests,json
from bs4 import BeautifulSoup
from pprint import pprint


Url = "https://webscraper.io/test-sites"
req = requests.get(Url)
# print(req)
soup = BeautifulSoup(req.text,"html.parser")
# pprint(soup)
main_data = soup.find("div",class_="container test-sites")
# pprint(main_data)
main_data_1 = main_data.find_all("div",class_="col-md-7 pull-right")
# print(main_data_1)
posstion = 0
i = 0
list_1 = []
for i in main_data_1:
    posstion += 1
    name = i.find("h2",class_="site-heading").get_text().strip()
    # print(name)
    link = i.find("h2",class_="site-heading").a["href"]
    link_1 = "https://webscraper.io/test-sites"+link
    # print(link_1)
    dic = {"posstion":posstion,"name":name,"link":link_1,}
    list_1.append(dic)
    # print(list_1)
    with open("Ecommerce.json","w") as file:
        json.dump(list_1,file,indent=4)
    print(list_1)    

