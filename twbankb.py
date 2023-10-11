# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:04:12 2023

@author: USER
"""

import requests

from bs4 import BeautifulSoup

import db

def getRate():
    
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    #use header 
    header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
        
    data = requests.get(url,headers = header)
    data.encoding = 'utf-8' #轉編碼
    data = data.text        #再轉文字
    
    
    
    soup = BeautifulSoup(data,'html.parser')
    #print(soup)
    
    rate = soup.find('table')

    allrate = rate.find('tbody') 

    trs = allrate.find_all('tr')

    for item in trs:
        tds = item.find_all('td')
        currency = tds[0].text.strip() #去前後空白
        currency = currency.split()    #從中分割 以空白為分割 分隔完為串列

        sql = "insert into rate(currency,buy,sell) values ('{}','{}','{}')".format(currency[0],tds[1].text.strip(),tds[2].text.strip())
        db.cur.execute(sql)
        db.conn.commit()

    db.conn.close()
    
getRate()       
  

