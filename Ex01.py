# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:20:04 2023

@author: USER
"""

from flask import Flask , render_template,request,redirect,url_for

from ctsnews import getNews

from twbank import getRate

import db

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    
    sql = "select title,link,photo_url from news limit 6"
    
    db.cur.execute(sql)
    db.conn.commit()
    allnews = db.cur.fetchall()     
    

    
    sql = "select * from product order by id desc limit 4"
    db.cur.execute(sql)
    allGoods = db.cur.fetchall()
    
    
    sql = "select name,photo_url,link,create_date from food order by create_date limit 4 "
    db.cur.execute(sql)
    db.conn.commit()
    data = db.cur.fetchall()    
    
    return render_template('index.html',**locals())


@app.route("/news")
def news():
    
    
    sql = "select title,link,photo_url from news"
    
    db.cur.execute(sql)
    db.conn.commit()
    allnews = db.cur.fetchall() 
    
    return render_template('news.html',**locals())
   
@app.route("/product")   
def pchome():
    
    sp = request.args.get('sprice')
    ep = request.args.get('eprice')
    
    if sp == None or ep == None or sp == '' or ep == '' :
        sql = "select * from product order by id desc"
    else:
        if sp.isdigit() and ep.isdigit():
            sql = "select * from product where onsale >= {} and onsale <= {} order by onsale".format(sp,ep)
        else:
            sql = "select * from product order by id desc"
    db.cur.execute(sql)
    allGoods = db.cur.fetchall()
    return render_template('product.html',**locals())
    

@app.route("/food")    
def getFood():
    sql = "select name,photo_url,link,create_date from food order by create_date "
    db.cur.execute(sql)
    db.conn.commit()
    data = db.cur.fetchall()
    return render_template('food.html',**locals())
    


@app.route("/contact")
def message():
    return render_template("contact.html")

@app.route("/addcontact",methods=['POST'])

def contact():
    if request.method == 'POST':
        username = request.form.get('name')
        title = request.form.get('title')
        email = request.form.get('email')
        content = request.form.get('content')
        modify_date = datetime.today()
        cdate = datetime.strftime(modify_date,'%Y-%m-%d')
        
        #新增資料到資料表
        
        sql = "insert into contact(subject,name,email,content,create_date) values('{}','{}','{}','{}','{}')".format(title,username,email,content,cdate)
        db.cur.execute(sql)
        db.conn.commit()
    return redirect(url_for('message'))    


@app.route('/twbank')
def bank():
    
    sql = "select currency,buy,sell from rate"
    
    db.cur.execute(sql)
    db.conn.commit()
    rate = db.cur.fetchall()     
    return render_template('twbank.html', **locals())
    
    


app.run()

 