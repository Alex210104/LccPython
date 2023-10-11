# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:59:03 2023

@author: USER
"""

import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',passwd='1234567890',database='myweb',auth_plugin='mysql_native_password',buffered=True)




cur = conn.cursor() #　dataset