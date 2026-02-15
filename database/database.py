import sqlite3
from flask import request, Blueprint

db_name = "swimmer_info.db"

cre = Blueprint("cre", __name__, )

def createTables():
    conn = sqlite3.connect(db_name)
    #connects to sqlite3 database and creates the database if it doesn't exist

    cursor = conn.cursor()
    #controls structure via cursor

    cursor.execute("""
        CREATE TABLE user (
            rankings_ID INTEGER NOT NULL UNIQUE PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            CHECK (length(rankings_ID) < 11 AND length(rankings_ID) > 3),
            CHECK (length(username) > 4 AND length(password) > 8 AND password LIKE '%[0-9]%')
                );
        """)


    cursor.execute("""
        CREATE TABLE race (
            race_ID INTEGER NOT NULL UNIQUE PRIMARY KEY,
            distance INTEGER NOT NULL,
            stroke TEXT NOT NULL,
            course TEXT NOT NULL,
            CHECK (race_ID < 36 AND race_ID > 0)
                );
        """)


    cursor.execute("""
        CREATE TABLE competition (
            comp_name TEXT NOT NULL UNIQUE PRIMARY KEY,
            venue TEXT               
                );
        """)


    cursor.execute("""
        CREATE TABLE goal (
            rankings_ID INTEGER NOT NULL,
            race_ID INTEGER NOT NULL,
            goal_time TIME,
            PRIMARY KEY (rankings_ID , race_ID),
            FOREIGN KEY (rankings_ID) REFERENCES user(rankings_ID),
            FOREIGN KEY (race_ID) REFERENCES race(race_ID)
                    );
        """)


    cursor.execute("""
        CREATE TABLE meet(
            comp_name TEXT NOT NULL,
            date DATE NOT NULL,
            target BOOL,
            PRIMARY KEY (comp_name , date),
            FOREIGN KEY (comp_name) REFERENCES competition(comp_name)
                );       
        """)


    cursor.execute("""
        CREATE TABLE result(
            rankings_ID INTEGER NOT NULL,
            race_ID INTEGER NOT NULL,
            comp_name TEXT NOT NULL,
            date DATE NOT NULL,
            entry_time TIME,
            final_time TIME,
            PRIMARY KEY (rankings_ID , race_ID , comp_name , date),
            FOREIGN KEY (rankings_ID) REFERENCES user(rankings_ID),
            FOREIGN KEY (race_ID) REFERENCES race(race_ID),
            FOREIGN KEY (comp_name) REFERENCES competition(comp_name),
            FOREIGN KEY (date) REFERENCES meet(date)
                );
        """)



@cre.route("/createuser", methods=["POST"])
def createUser():
    with sqlite3.connect() as conn:
        formDetails = request.form
        rankings_ID = formDetails.get("SE_ID")
        name  = formDetails.get("name")
        email = formDetails.get("email")
        password = formDetails.get("password")
        conn.execute("INSERT INTO user (rankings_ID, username, password, name) VALUES (?, ?, ?, ?)")
        conn.commit()


#createTables()
#createUser()