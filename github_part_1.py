# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:09:42 2021

@author: Ertuğrul Furkan Düzenli
"""
import pandas as pd
import datetime as dt

import bs4
import requests
from bs4 import BeautifulSoup

def real_time_price(symbol):
    url = ('https://finance.yahoo.com/quote/') + symbol + ('/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAINGLolHcuHio-RL9CxZfo-oVtwUkHS8YcK0YIVrQ5xq_lIZ-fIAs3-ES7u3LEWmVJzbO_TWMRxthn-ztc1PdHz_fZpWossP2BfNkD36qNOb5bVSIYCNi9do9p3gNPWEDkG-EcjPZfyVt4ByNTINX2nqoTKFGg8tvjPk8dKWJRxS')
    r = requests.get(url)
    web_content = BeautifulSoup(r.text, 'lxml')
    web_content = web_content.find('div', {"class":'My(6px) Pos(r) smartphone_Mt(6px)'})
    web_content = web_content.find('span').text

    return web_content

NASDAQ = ['TSLA', 'AAPL', 'BNTX', 'KO']
web_content = real_time_price('TSLA')

for step in range(1,101):   
    
    price = []
    col = []
    time_stamp = dt.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    
    for symbol in NASDAQ:
        price.append(real_time_price(symbol))
        
    col = [time_stamp]
    col.extend(price)
    
    df = pd.DataFrame(col)
    
    df = df.T
    
    df.to_csv('real time stock data.csv', mode = 'a', header = False)
    print(col)
    
    