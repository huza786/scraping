import requests
from bs4 import BeautifulSoup
print("Initialted")
url = "https://www.scrapethissite.com/pages/simple/"
req = requests.get(url)

# Check if the request was successful
if req.status_code == 200:
    print("Successful request")
    soup = BeautifulSoup(req.content, "html.parser")
    print("Web scraping first phase completed")
    # Adjust the selector based on the actual structure of the webpage
    title = soup.find_all("div", class_="col-md-4 country")
    print(title)
    with open("sample.html","w") as f:
        
       
    # Print the titles
      for item in title:
        f.write(item.text.strip()+"\n")
        print(item.text.strip())
else:
    print(f"Failed to retrieve the webpage. Status code: {req.status_code}")
