#!/bin/python
#coding=UTF-8
# pip install Flask
#pip install flask-mysql
from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)







@app.route("/")
def hello():
    return "Hello World!"



if __name__ == '__main__':
    # **IMPORTANT** In demo need to recover to 80 port
    app.run(host='0.0.0.0', port=8009)



