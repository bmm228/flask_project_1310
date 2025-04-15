from flask import Flask, redirect, url_for, render_template, request
import sqlite3
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
        return render_template('home.html')


@app.route('/enternew')
def newCustomer():
    return render_template('book.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            checkIn = request.form['checkIn']
            checkOut = request.form['checkOut']
            roomType = request.form['roomType']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO finalProject (name,checkIn,checkOut,roomType) VALUES('{0}','{1}','{2}','{3}')".format(name,checkIn,checkOut,roomType))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result.html",msg = msg, name = name, checkIn = checkIn, checkOut = checkOut)
            con.close()


@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from finalProject")
    rows = cur.fetchall();
    return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.run(debug = True)