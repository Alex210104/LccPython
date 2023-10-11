# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:02:43 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
import db

def getNews():
    

    url = "https://news.cts.com.tw/real/index.html"
    
    header = {
    
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    
    }
    
    data = requests.get(url,headers=header)
    data.encoding = 'utf-8'
    data = data.text
    
    soup = BeautifulSoup(data,'html.parser')
    
    news = soup.find(id='newslist-top')
    
    allNews = news.find_all('a')
    
    
    for item in allNews:
        
        
        title = item.get('title')
        link = item.get('href')
        img = item.find('img')
        if not img == None:
            if img.get('data-src') == None:
                photo_url = "https://www.cts.com.tw/images/2018cts/news_default.jpg"

            else:    
                photo_url = img.get('data-src')
        else:
            photo_url = "https://www.cts.com.tw/images/2018cts/news_default.jpg"
        
               
        sql = "insert into news(title,link,photo_url) values('{}','{}','{}')".format(title,link,photo_url)
        db.cur.execute(sql)
        db.conn.commit()
        
    db.conn.close()   


getNews()        
        
      
            












