# =================================
# SaveGo AI V7.5
# Database Module
# =================================


import sqlite3



DATABASE = "savego.db"



# 创建数据库

def init_db():

    conn = sqlite3.connect(
        DATABASE
    )


    cursor = conn.cursor()



    # 收藏表

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS favorites(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            product TEXT

        )
        """
    )



    # 搜索历史表

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            keyword TEXT

        )
        """
    )



    conn.commit()

    conn.close()





# 添加收藏

def add_favorite(
        username,
        product
):


    conn = sqlite3.connect(
        DATABASE
    )


    cursor = conn.cursor()



    cursor.execute(

        """
        INSERT INTO favorites
        (username,product)

        VALUES(?,?)

        """,

        (
            username,
            product
        )

    )


    conn.commit()

    conn.close()





# 获取收藏

def get_favorites(
        username
):


    conn = sqlite3.connect(
        DATABASE
    )


    cursor = conn.cursor()



    cursor.execute(

        """
        SELECT product
        FROM favorites
        WHERE username=?

        """,

        (
            username,
        )

    )



    data = cursor.fetchall()


    conn.close()



    return [

        item[0]

        for item in data

    ]





# 保存搜索历史

def add_history(
        username,
        keyword
):


    conn = sqlite3.connect(
        DATABASE
    )


    cursor = conn.cursor()


    cursor.execute(

        """
        INSERT INTO history
        (username,keyword)

        VALUES(?,?)

        """,

        (
            username,
            keyword
        )

    )


    conn.commit()

    conn.close()
