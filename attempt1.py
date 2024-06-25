import requests

from bs4 import BeautifulSoup
def saveDataToFile(url,path):

   
    req=requests.get(url)
    soup=BeautifulSoup(req.text,'html.parser')
    s= soup.find("h2")


    with open(path,"w") as f:
        
        f.write(s.text)
req= requests.get("http://olympus.realpython.org/profiles/aphrodite")
saveDataToFile("http://olympus.realpython.org/profiles/aphrodite","sample.html")
soup=BeautifulSoup(req.content,"html.parser")

name= soup.find("h2")
print(
soup.getText

)
print(name)