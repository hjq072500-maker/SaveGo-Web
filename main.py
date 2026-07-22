from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI(
    title="SaveGo AI V7.0",
    description="智能比价购物助手"
)


# 允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProductRequest(BaseModel):
    keyword:str



@app.get("/")
def home():

    return {
        "message":"SaveGo AI V7.0 后端运行成功"
    }



@app.post("/search")
def search_product(
        data:ProductRequest
):

    keyword=data.keyword


    return {

        "product":keyword,

        "score":92,

        "price":7499,

        "platforms":[
            "京东",
            "淘宝",
            "亚马逊"
        ],

        "advice":
        "建议比较价格后购买"

    }



@app.get("/ai")
def ai_assistant():

    return {

        "assistant":
        "SaveGo AI购物助手已上线"

    }
