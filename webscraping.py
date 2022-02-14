from cgitb import text
from turtle import title
from bs4 import BeautifulSoup as bs
import requests
class storage:
    def __init__(self):
        self.updatedprices={}
        self.update()
        self.store={}
    def update(self):
        html=requests.get('https://gadgets.ndtv.com/finance/crypto-currency-price-in-india-inr-compare-bitcoin-ether-dogecoin-ripple-litecoin').text
        soup=bs(html,'lxml')
        body=soup.find_all('tbody')
        coin_names=soup.find_all('tr',class_='_cptbltr')
        for i in coin_names:
            coin_name=i.find('span',class_="crysrtnm")
            price=i.find('td',class_='_rft _cpr')
            if coin_name and price:
                coin_name=coin_name.text
                price=price.text.strip()[2:]
                n=len(coin_name)
                coin=coin_name[1:n-1]
                price=float(''.join(price.split(',')))
                self.updatedprices[coin]=price
    def insert(self,name,url):
        self.store[name]=url
        return self.store
    def find(self):
        html=requests.get('https://www.moneycontrol.com/news/business/cryptocurrency/top-cryptocurrency-news-today-the-biggest-moves-in-nfts-bitcoin-crypto-rules-and-more-18-8085231.html').text
        soup=bs(html,'lxml')
        titletext=soup.find_all('div',class_='essen_desclink')
        for i in titletext:
            name=i.find('p',class_='essen_title').text
            url=i.find('a')['href']
            self.insert(name,url)
x=storage()
print(x.updatedprices)