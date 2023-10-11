# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:51:15 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup

def getRate():

    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    
    header = {
    
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    
    }
    
    data = requests.get(url,headers=header)
    data.encoding = 'utf-8'
    data = data.text
    
    soup = BeautifulSoup(data,'html.parser')
    
    rate = soup.find('table')
    
    
    trs = rate.find_all('tr')
    
    trs = trs[2:]
    
    rate = list()
    
    for item in trs:
        tds = item.find_all('td')
        currency = tds[0].text.strip()
        currency = currency.split() # 為什麼要使用 split  因為文字中間有空白，直接切
       
        temp = list()
        temp.append(currency[0])
        temp.append(tds[1].text.strip())
        temp.append(tds[2].text.strip())
        rate.append(temp)
        
    return rate    
        
        
        
        
        
        
        

