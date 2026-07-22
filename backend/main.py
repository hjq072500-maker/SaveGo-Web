# ==================================
# SaveGo AI Final Backend
# ==================================

from fastapi import FastAPI
from pydantic import BaseModel


from database import (
    init_db,
    connect
)


from products import products


from ai_engine import recommend


from auth import (
    register,
    login
)



app = FastAPI(

    title="SaveGo AI",

    description="AI智能购物助手",

    version="Final 1.0"

)



# 初始化数据库

init_db()



# =========================
# 数据模型
# =========================


class SearchRequest(BaseModel):

    keyword:str




class RecommendRequest(BaseModel):

    keyword:str

    budget:int



class UserRequest(BaseModel):

    username:str

    password:str




class FavoriteRequest(BaseModel):

    username:str

    product:str





# =========================
# 首页
# =========================


@app.get("/")

def home():

    return {

        "name":"SaveGo AI",

        "version":"Final",

        "status":"running"

    }





# =========================
# 商品搜索
# =========================


@app.post("/search")

def search(
    req:SearchRequest
):


    result=[]


    for p in products:


        if (

            req.keyword.lower()

            in

            p["name"].lower()

            or

            req.keyword.lower()

            in

            p["category"].lower()

        ):

            result.append(p)



    return {

        "keyword":req.keyword,

        "count":len(result),

        "products":result

    }





# =========================
# AI推荐
# =========================


@app.post("/recommend")

def ai_recommend(

    req:RecommendRequest

):


    result=recommend(

        products,

        req.budget

    )


    return {


        "keyword":req.keyword,

        "budget":req.budget,

        "recommendation":

        result[:3]

    }





# =========================
# 用户注册
# =========================


@app.post("/register")

def user_register(

    req:UserRequest

):


    return {

        "success":

        register(

            req.username,

            req.password

        )

    }





# =========================
# 用户登录
# =========================


@app.post("/login")

def user_login(

    req:UserRequest

):


    return {

        "login":

        login(

            req.username,

            req.password

        )

    }





# =========================
# 收藏商品
# =========================


@app.post("/favorite")

def favorite(

    req:FavoriteRequest

):


    conn=connect()

    cursor=conn.cursor()



    cursor.execute(

        """
        INSERT INTO favorites
        (
        username,
        product
        )
        VALUES
        (?,?)

        """,

        (
            req.username,

            req.product

        )

    )


    conn.commit()

    conn.close()



    return {

        "message":"收藏成功"

    }





# =========================
# 查看收藏
# =========================


@app.get("/favorites/{username}")

def favorites(

    username:str

):


    conn=connect()

    cursor=conn.cursor()



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


    data=cursor.fetchall()


    conn.close()



    return {

        "username":username,

        "favorites":

        [

            x[0]

            for x in data

        ]

    }
