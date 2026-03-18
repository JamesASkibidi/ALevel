from app import db_connect

cx = db_connect()

users = cx.execute("SELECT * FROM users").fetchall()

busses = cx.execute("SELECT * FROM busses").fetchall()

name = cx.execute("""
                
        SELECT users.first_name
        FROM users
        JOIN booking ON booking.u_id = users.u_id
        JOIN busses ON busses.bu_id = booking.bu_id
        WHERE busses.registration = 'MC53BUS'
         
                          
                          
        """)

print(name)
