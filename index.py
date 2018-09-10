#!/bin/python
#coding=UTF-8
#pip install Flask
#pip install flask-mysql
#pip install multiprocessing
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from multiprocessing import Pool
from multiprocessing import cpu_count
import socket
import time
from threading import Timer
import ConfigParser

app = Flask(__name__)

#global variables
isLoop = True
db = {}


def f(x):
    global isLoop
    while isLoop:
        x*x

def stopStress(pool):
    try:
        global isLoop
        isLoop = False
        pool.terminate()
        pool.close()
        print('[INFO]: STOP STRESS')
    except:
        print("[ERROR]: Stop pools of processes fail")

def stressAllProcesses(stopSec):
    try:
        process = cpu_count()
        print ('[INFO]: Utilizing %d cores\n' % process)
        pool = Pool(process)
        #set stopping time
        t = Timer(stopSec, stopStress, [pool])
        t.start()
        #start stress
        pool.map(f, range(process))
    except:
        print("[ERROR]: Processes execute fail.")

def connectMySQL():
    try:
        mysql = MySQL()
        global db
        app.config['MYSQL_DATABASE_USER'] = db['user']
        app.config['MYSQL_DATABASE_PASSWORD'] = db['password']
        app.config['MYSQL_DATABASE_DB'] = db['dbName']
        app.config['MYSQL_DATABASE_HOST'] = db['host']
        mysql.init_app(app)
        return mysql.connect()
    except MySQL.Error as e:
        print('[ERROR]: %s' %(e))
        return None

def getVideos():
    try:
        conn = connectMySQL()
        cursor = conn.cursor()
        cursor.execute("SELECT * from video")
        videos = cursor.fetchall()
        json = {}
        for record in videos:
            json[str(record[1])] = str(record[2])
        return json
    except:
        print("[WARN]: get video fail")
        return None


def initalData():
    data = {}
    try:
        #**need to validate*** get private ip
        data['IP'] = socket.gethostbyname(socket.gethostname())
        #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #s.connect(("8.8.8.8", 80))
        #print(s.getsockname()[0])
        #s.close()
    except:
        print("ERROR]: Get private IP fail")

    data['stress_stop_mins'] = 6
    #get vedios from DB
    data['videos'] = getVideos()
    return data

def indexTemplate():
    data = initalData()
    return render_template('./index.html', **data)

@app.route("/stress")
def stress():
    #Todo stress
    data = initalData()
    data['stress_stop_mins'] = request.args.get('mins', default = 1, type = int)
    
    time.sleep(1)
    print("[INFO]: Start Stress for %d minutes." %(int(data['stress_stop_mins'])) )
    stressAllProcesses(int(data['stress_stop_mins']) * 60)
    
    return "Stress Finish!"




@app.route("/")
def index():
    return indexTemplate()



if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read('default.conf')
    global db
    db['user'] = config.get('DB_MYSQL', 'user')
    db['password'] = config.get('DB_MYSQL', 'password')
    db['dbName'] = config.get('DB_MYSQL', 'dbName')
    db['host'] = config.get('DB_MYSQL', 'host')

    IP = config.get('WEB_HOST', 'IP')
    Port = config.get("WEB_HOST", "Port")
    app.run(IP, Port)



