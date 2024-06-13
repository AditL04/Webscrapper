from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

visitedurls  = set()

def spiderurls(url,keyword):
    try:
        response=requests.get(url)
    except:
        print(f'request failed {url}')
        return
    
    if response.status_code==200:
        soup=BeautifulSoup(response.content, 'html.parser')

        atag=soup.find_all('a')
        urls=[]
        for tag in atag:
            href=tag.get("href")
            if href is not None and href !="":
                urls.append(href)
        for urls2 in urls:
            if urls2 not in visitedurls:
                visitedurls.add(urls2)
                url_join=urljoin(url,urls2)
                if keyword in url_join:
                    print(url_join)
                    spiderurls(url_join,keyword)
                else:
                    pass


    


   

url=input("input a url to scrape")
keyword=input("a keyword youre looking for")
spiderurls(url, keyword)

