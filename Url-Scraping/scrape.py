from bs4 import BeautifulSoup
import requests
import re
 
def scraping(website):
    req = requests.get(url)  #req = response object
    soup = BeautifulSoup(req.text, 'lxml')
    lst = []

    for link in soup.find_all('a', href=True):
       #if url not in link.get("href"):
        lst.append(link.get('href'))
    
    lst = list(dict.fromkeys(lst))
    output = [idx for idx in lst if not idx.startswith(("/","#")) and "." in idx] 
    
    return output
    
if __name__ == '__main__': 
    url = input("Enter a website link: ")
    urlList = scraping(url)
    print(*urlList, sep= "\n")
    input("\nEnter any key to quit!\n")   
    