from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import uvicorn


# =========================
# SaveGo AI V7.0
# Backend API
# =========================


app = FastAPI(
    title="SaveGo AI V7.0",
    description="智能比价购物助手",
    version="7.0"
)


# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# =========================
# 数据模型
# =========================

class ProductRequest(BaseModel):
    keyword: str



# =========================
# 首页
# =========================

@app.get("/")
def home():

    return {
        "name": "SaveGo AI V7.0",
        "status": "running",
        "message": "智能比价购物助手在线"
    }



# =========================
# 健康检查
# =========================

@app.get("/health")
def health():

    return {
        "status":"ok"
    }



# =========================
# 商品搜索
# =========================

@app.post("/search")
def search_product(
        request: ProductRequest
):

    keyword = request.keyword


    # 后续接入淘宝/京东/API
    products = [

        {
            "name":keyword,
            "price":"暂无价格",
            "platform":"SaveGo AI"
        }

    ]


    return {

        "keyword":keyword,
        "count":len(products),
        "products":products

    }



# =========================
# AI助手
# =========================

@app.get("/ai")
def ai_assistant():

    return {

        "assistant":"SaveGo AI",

        "reply":
        "你好，我是你的智能购物助手，可以帮助比较商品价格、分析优惠。"

    }



# =========================
# Render启动
# =========================

if __name__=="__main__":

    port=int(
        os.environ.get(
            "PORT",
            8000
        )
    )


    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )
