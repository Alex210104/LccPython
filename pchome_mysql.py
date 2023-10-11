# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:41:01 2023

@author: USER
"""


import requests
import json
import time

import db

import datetime

url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results'

header = {
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    
param = {

    'q':'可口可樂',
'page':'1',
'sort':'sale/dc'    
    
    } 

for i in range(1,6):
    
    param['page'] = str(i)

    pchome = requests.get(url,headers=header,params=param).text
    
    pchome = json.loads(pchome)
    
    allgoods = pchome['prods']
    
    
    for item in allgoods:
        img = 'https://cs-c.ecimg.tw/' +item['picB']
        name = item['name']
        info = item['describe']
        price = item['price']
        link = "https://24h.pchome.com.tw/prod/" + item['Id']
        
        sql = "select * from product where platform='Pchome' and link='{}'".format(link)
        
        db.cur.execute(sql)
        db.conn.commit()

        
        if db.cur.rowcount == 0:  #no product
        
            print(link)
        
            today = datetime.datetime.today()
            now = today.strftime('%Y-%m-%d')
            
            sql = "insert into product(platform,title,photo_url,link,price,onsale,create_date) values(%s,%s,%s,%s,%s,%s,%s)"     
            db.cur.execute(sql,['Pchome',name,img,link,price,price,now])
            db.conn.commit()
            
    
    time.sleep(2)
db.conn.close()    
    



  