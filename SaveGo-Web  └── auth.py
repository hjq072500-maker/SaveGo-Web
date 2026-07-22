# =================================
# SaveGo AI V8.0
# User Authentication
# =================================


import sqlite3
import hashlib


DATABASE = "savego.db"



def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def create_user(
        username,
        password
):

    conn = sqlite3.connect(
        DATABASE
    )

    cursor = conn.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE,

            password TEXT

        )
        """
    )


    try:

        cursor.execute(
            """
            INSERT INTO users
            (username,password)

            VALUES(?,?)

            """,

            (
                username,
                hash_password(password)
            )

        )

        conn.commit()

        result=True


    except:

        result=False



    conn.close()


    return result




def login_user(
        username,
        password
):

    conn = sqlite3.connect(
        DATABASE
    )


    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=?
        AND password=?

        """,

        (
            username,
            hash_password(password)
        )

    )


    user = cursor.fetchone()


    conn.close()


    return user is not None
