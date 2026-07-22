from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI(
    title="SaveGo AI V7.1",
    description="智能比价购物助手",
    version="0.1.1"
)


# =====================
# 数据模型
# =====================

class ProductRequest(BaseModel):
    keyword: str


class Product(BaseModel):
    name: str
    price: str
    platform: str


# =====================
# 首页
# =====================

@app.get("/")
def home():
    return {
        "name": "SaveGo AI V7.1",
        "status": "running",
        "message": "智能比价购物助手 API"
    }


# =====================
# 商品搜索 API
# =====================

@app.post("/search")
def search_product(req: ProductRequest):

    keyword = req.keyword.strip()


    # 模拟商品数据库
    products_db = [

        {
            "name": "Apple MacBook Air M3 13英寸",
            "price": "7999元",
            "platform": "Apple官方"
        },

        {
            "name": "MacBook Air M3 笔记本电脑",
            "price": "7499元",
            "platform": "京东"
        },

        {
            "name": "Apple MacBook Air M3 午夜色",
            "price": "7599元",
            "platform": "淘宝"
        },

        {
            "name": "MacBook Pro M3",
            "price": "10999元",
            "platform": "天猫"
        },

        {
            "name": "iPhone 16 Pro Max",
            "price": "9999元",
            "platform": "Apple官方"
        },

        {
            "name": "iPhone 16 Pro",
            "price": "7999元",
            "platform": "京东"
        },

        {
            "name": "小米 SU7 电动车",
            "price": "215900元",
            "platform": "小米汽车"
        }

    ]


    results = []


    # 搜索匹配
    for product in products_db:

        if keyword.lower() in product["name"].lower():

            results.append(product)



    # 没搜索到时返回默认结果

    if len(results) == 0:

        results.append(
            {
                "name": keyword,
                "price": "暂无价格",
                "platform": "SaveGo AI"
            }
        )


    return {

        "keyword": keyword,

        "count": len(results),

        "products": results

    }



# =====================
# AI 助手接口
# =====================

@app.get("/ai")
def ai_assistant():

    return {

        "assistant": "SaveGo AI",

        "message": "你好，我可以帮助你分析商品价格和推荐购买方案"

    }
