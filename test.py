# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 21:17:02 2023

@author: USER
"""

import db

sql = "select title,photo_url from product order by id desc limit 2"
db.cur.execute(sql)
allGoods = db.cur.fetchall()

print(allGoods)