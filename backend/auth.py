# ==================================
# SaveGo AI Final
# User Authentication
# ==================================

import hashlib
from database import connect



def encrypt(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def register(
        username,
        password
):

    conn = connect()

    cursor = conn.cursor()


    try:

        cursor.execute(
            """
            INSERT INTO users
            (
            username,
            password
            )
            VALUES
            (?,?)
            """,

            (
                username,
                encrypt(password)
            )
        )


        conn.commit()

        result=True


    except Exception:

        result=False



    conn.close()


    return result





def login(
        username,
        password
):

    conn=connect()

    cursor=conn.cursor()


    cursor.execute(

        """
        SELECT *
        FROM users
        WHERE username=?
        AND password=?

        """,

        (
            username,
            encrypt(password)
        )

    )


    user=cursor.fetchone()


    conn.close()


    return user is not None
