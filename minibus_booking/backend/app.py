#flask is the frontend framework for python
#handles webpage logic

from flask import Flask , render_template , request , redirect

import sqlite3


##Webpage Logic

app = Flask(__name__)

DATABSE = "minibus_booking/backend/bus_booking.db"


def db_connect():

    cx = sqlite3.connect(DATABSE)
    cx.row_factory = sqlite3.Row
    cx.execute("PRAGMA foreign_keys = ON;")
    return cx

#home page "/" - app route is how pages are navigated
#GET method to retrieve data

@app.route("/" , methods = ["GET"])


#function to retreive all data from database - to use in homepage

def index():
    cx = db_connect()

    users = cx.execute("SELECT * FROM users").fetchall()

    busses = cx.execute("SELECT * FROM busses").fetchall()
    
    bookings = cx.execute("""
                
        SELECT booking.bo_id , users.first_name, users.last_name , busses.registration  , booking.date
        FROM booking
        JOIN users ON booking.u_id = users.u_id
        JOIN busses ON booking.bu_id = busses.bu_id
                          
                          
        """).fetchall()
    
    cx.close()

    #sends data to index.html

    return render_template("minibus_booking/frontend/templates/index.html" , users = users , busses = busses , bookings = bookings)


@app.route("/add_user" , methods = ["POST"])

def add_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    cx = db_connect()
    cx.execute("INSERT into users (first_name, last_name , email) VALUES ( ?, ? , ?)",
               (first_name, last_name , email))
    
    cx.commit()
    cx.close()
    return redirect("/")

@app.route("/add_bus" , methods = ["POST"])
def add_bus():
    model = request.form["model"]
    registration = request.form["registration"]
    seating = request.form["seating"]
    cx = db_connect()
    cx.execute("INSERT into busses (model, registration, seating) VALUES ( ? , ? , ?)",
               (model, registration, seating))
    
    cx.commit()
    cx.close()
    return redirect("/")

@app.route("/create_booking" , methods = ["POST"])
def create_booking():
    u_id = request.form["u_id"]
    bu_id = request.form["bu_id"]
    date = request.form["date"]
    cx = db_connect()
    cx.execute("INSERT into booking (u_id, bu_id, date) VALUES ( ?, ? , ?)",
               (u_id , bu_id , date))
    
    cx.commit()
    cx.close()
    return redirect("/")
    

app.run()