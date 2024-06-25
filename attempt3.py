import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
def fetchAndSaveToFile(url,path):
    res=requests.get(url)

    soup=BeautifulSoup(res.text,'html.parser')      
    cards=soup.find_all('div',class_="card thumbnail")
    with open(path,'w',encoding='utf-8') as f:
       for card in cards:
        f.write(card.getText())
        

fetchAndSaveToFile(url,"output.html")