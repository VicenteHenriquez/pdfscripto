from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
#create api flask app
app = Flask(__name__)
conn = sqlite3.connect("pdfs.db", check_same_thread = False)
c = conn.cursor()

def getultimo():
    sql = "SELECT * FROM datos ORDER BY id DESC LIMIT 1"
    c.execute(sql)
    ultimo = c.fetchone()
    return ultimo

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST': #puede variar segun como reciba la info de pdf
        sistop1 = str(request.form.get('sistop',False))
        ver1 = str(request.form.get('ver'))
        iprec1 = str(request.form.get('iprec'))
        passwd1 = str(request.form.get('passwd'))
        sql = """INSERT INTO datos (sistema,version,ip,pass) VALUES (?,?,?,?)"""
        c.execute(sql,(sistop1,ver1,iprec1,passwd1,))
        conn.commit()
        last = getultimo()
        sistop = last[1]
        ver = last[2]
        iprec = last[3]
        passwd = last[4]
        return render_template('main.html',sistop=sistop,ver=ver,iprec=iprec,passwd=passwd)
    return 'Ok'

if __name__ == '__main__':
	app.run(debug=True)