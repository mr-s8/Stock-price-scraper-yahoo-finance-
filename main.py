import requests
from bs4 import BeautifulSoup
from lxml import etree


def getPrice(symbol):
    url = "https://finance.yahoo.com/quote/"+symbol+"?p="+symbol+"&.tsrc=fin-srch"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    data = etree.HTML(str(soup))

    res = [data.xpath(
        "//*[@id=\"quote-header-info\"]/div[3]/div[1]/div[1]/fin-streamer[2]/span/text()"), data.xpath("//*[@id=\"quote-header-info\"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()"), data.xpath(
        "//*[@id=\"quote-header-info\"]/div[3]/div[1]/div[1]/fin-streamer[3]/span/text()")]

    return res
  
  
  
