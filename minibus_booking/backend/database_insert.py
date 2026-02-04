import sqlite3

cx = sqlite3.connect("minibus_booking/backend/buss_booking.db")

cu = cx.cursor()

cu.execute("PRAGMA foreign_keys = ON;")

cu.executemany("""
INSERT INTO users (first_name, last_name, email) 
VALUES (?, ?, ?)
""", [
    ("Raff", "Shannon", "raffs@gmail.com" ),
    ("Joe", "Ephgrave", "joee@gmail.com"),
    ("Pete", "lee", "petelee@hotmail.com")
])



cu.executemany("""
INSERT INTO busses (model, registration, seating) 
VALUES (?, ?, ?)
""", [
    ("MC300", "MC53BUS", 12 ),
    ("SK80", "SK60BUS", 8),
    ("VW2", "VW55BUS", 20)
])

cu.executemany("""
INSERT INTO booking (u_id, bu_id, date) 
VALUES (?, ?, ?)
""", [
    (1,2,"28-01-26" ),
    (2,3,"26-01-26" ),
    (1,1,"28-04-26" )
])


cx.commit()

cx.close()

print('Data commited')



# cu.executemany("""INSERT INTO busses VALUES (1 , "MC300" , "TX 110 BUS" , 12)""")