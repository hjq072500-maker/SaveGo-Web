from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from product_api import (
    search_products,
    analyze_products
)


app = FastAPI(

    title="SaveGo AI V7.1",

    description="智能比价购物助手",

    version="7.1"

)



# ==========================
# 跨域设置
# ==========================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)



# ==========================
# 数据模型
# ==========================

class ProductRequest(BaseModel):

    product: str



# ==========================
# 首页检测
# ==========================

@app.get("/")
def home():

    return {

        "name":"SaveGo AI",

        "version":"V7.1",

        "status":"running",

        "message":"智能购物助手在线"

    }



# ==========================
# 商品搜索接口
# ==========================

@app.post("/search")
def search_product(

    req: ProductRequest

):


    # 获取商品数据

    products = search_products(

        req.product

    )


    # AI分析

    result = analyze_products(

        products

    )


    return {


        "query":

        req.product,


        "result":

        result


    }



# ==========================
# AI助手接口
# ==========================

@app.get("/ai")
def ai_assistant():


    return {


        "assistant":

        "SaveGo AI购物助手",


        "version":

        "V7.1",


        "functions":[

            "商品搜索",

            "价格比较",

            "智能评分",

            "购买建议"

        ]

    }



# ==========================
# 健康检测
# ==========================

@app.get("/health")
def health():

    return {

        "status":"ok"

    }
