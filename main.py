from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="SaveGo AI V7.1",
    description="智能比价购物助手"
)


# 允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


class ProductRequest(BaseModel):
    product:str



@app.get("/")
def home():

    return {
        "name":"SaveGo AI",
        "version":"V7.1",
        "status":"running"
    }



@app.post("/search")
def search_product(
    req:ProductRequest
):

    product=req.product


    # 当前模拟AI评分
    # 后续接真实商品API

    result={

        "product":product,

        "score":92,

        "price_analysis":{

            "lowest_price":"¥6999",

            "platforms":[
                "京东",
                "淘宝",
                "拼多多"
            ]

        },


        "recommendation":
        "价格合理，建议购买"


    }


    return result




@app.get("/ai")
def ai():

    return {

        "assistant":
        "SaveGo AI购物助手已上线",

        "features":[
            "价格比较",
            "商品评分",
            "降价提醒"
        ]

    }
