import requests
from bs4 import BeautifulSoup
from lxml import etree


def getPrice(symbol):
    url = "https://finance.yahoo.com/quote/"+stonk+"?p="+stonk+"&.tsrc=fin-srch"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    #idk why but i think wihtout passing the user-agent header i am getting delayed data
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    data = etree.HTML(str(soup))

    res = [data.xpath("//*[@id=\"quote-header-info\"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()")[0],
           data.xpath("//*[@id=\"quote-header-info\"]/div[3]/div[1]/div[1]/fin-streamer[2]/span/text()")[0], 
           data.xpath("//*[@id=\"quote-header-info\"]/div[3]/div[1]/div[1]/fin-streamer[3]/span/text()")[0]]

    return res
  
  
  
#no guarantee that this works a 100%
