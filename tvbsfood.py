# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import db
import requests
from bs4 import BeautifulSoup

url = "https://supertaste.tvbs.com.tw/food"

header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'   
    }
    
foods = requests.get(url,headers=header).text
    
soup = BeautifulSoup(foods,'html.parser')    
allFoods = soup.find('div',class_= 'article__content' )

a = allFoods.find_all('a')


#find find_all 抓標籤          get 抓屬性
for item in a :
    link = item.get('href')
    link = "https://supertaste.tvbs.com.tw" + link
    title = item.find('h3').text.strip()
    post_date = item.find('span').text.strip()
    photo_url = item.find('img').get('data-original')
    
    sql = "select * from food where link='{}'".format(link)
    db.cur.execute(sql)
    db.conn.commit()  #立即執行
        

    if db.cur.rowcount == 0:  #no product
    
        sql = "insert into food(name,photo_url,link,create_date) values(%s,%s,%s,%s)"     
        db.cur.execute(sql,[title,photo_url,link,post_date])
        db.conn.commit()
    

db.conn.close()




