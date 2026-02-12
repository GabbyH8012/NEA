import sqlite3


class DatabaseHandler:
#defining the database handler class

    def __init__(self, db_name = "swimmer_info.db"):
        self.db_name = db_name
    #creating the constructor for the objects to be made

    def connect(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor
        return cursor
    #connects to sqlite3 database and creates the database if it doesn't exist
    #controls structure via cursor

    def createTables(self):
        with self.connect() as cursor:
            
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

