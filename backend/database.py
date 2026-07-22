import sqlite3


DB="savego.db"



def connect():

    return sqlite3.connect(DB)



def init_db():

    conn=connect()

    cursor=conn.cursor()



    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY,

    username TEXT UNIQUE,

    password TEXT

    )
    """
    )



    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS favorites(

    id INTEGER PRIMARY KEY,

    username TEXT,

    product TEXT

    )
    """
    )


    conn.commit()

    conn.close()
