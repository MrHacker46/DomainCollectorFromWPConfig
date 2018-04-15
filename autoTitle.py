# -*- coding: utf-8 -*-
import MySQLdb as db
import os
# Thirdparty modules installation required!
# Linux: pip install MySQL-python
# Windows: download binary executable of MySQLdb from the repository listing
PORT = 3306
tableprefix = ''
def extract(fileName):
    db = ''
    user = ''
    password = ''
    host = ''
    lines = open(fileName, 'r').read().split('\n')
    try:
        for i in lines:
            if 'DB_NAME' in i:
                j = i.split("'")
                db = j[3]
            if 'DB_USER' in i:
                j = i.split("'")
                user = j[3]
            if 'DB_PASSWORD' in i:
                j = i.split("'")
                password = j[3]
            if 'DB_HOST' in i:
                j = i.split("'")
                host = j[3]
            if '$table' in i:
                j = i.split("'")
                tableprefix = j[1]
        HOST = host
        USER = user
        PASSWORD = password
        DB = db
        getIT(tableprefix, HOST, USER, PASSWORD, DB)
    except:
        print 'Configuration File Invalid!'
def getIT(pref, HOST, USER, PASSWORD, DB):
    try:
        connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
        dbhandler = connection.cursor()
        query = "select option_value from " + pref + 'options where option_name = "siteurl"'
        dbhandler.execute(query)
        result = dbhandler.fetchall()
        open('domainList.txt','a+').write(result[0][0] + '\n')
    except:
        print 'db error'
for i in os.listdir(os.getcwd()):
    if os.path.isfile(i):
        if i == 'domainList.txt':
            continue
        extract(i)
print 'Done! See the domainList.txt file for domains!'
