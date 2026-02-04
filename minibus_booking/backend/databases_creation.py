import sqlite3

cx = sqlite3.connect("minibus_booking/backend/buss_booking.db")

cu = cx.cursor()

cu.execute("""
CREATE TABLE IF NOT EXISTS users (
    u_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL,
    email TEXT NOT NULL           
  
)           
""")

cu.execute("""
CREATE TABLE IF NOT EXISTS busses (
    bu_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT NOT NULL, 
    registration TEXT NOT NULL,
    seating INTEGER NOT NULL           
  
)           
""")



cu.execute("""
CREATE TABLE IF NOT EXISTS booking (
    bo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    u_id INTEGER NOT NULL,
    bu_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (u_id) REFERENCES users(u_id)   
    FOREIGN KEY (bu_id) REFERENCES busses(bu_id)        
  
)           
""")


cx.commit()

cx.close()

# cu.execute("INSERT INTO busses VALUES ()")

