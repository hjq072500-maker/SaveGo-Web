from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="SaveGo AI API V7.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


products = [

{
"name":"iPhone 16 Pro",
"price":7499,
"score":92,
"platform":"3个平台比较"
},

{
"name":"MacBook Air M4",
"price":8999,
"score":95,
"platform":"4个平台比较"
},

{
"name":"小米手机",
"price":2999,
"score":88,
"platform":"5个平台比较"
}

]


@app.get("/")
def home():

    return {
        "status":"SaveGo AI V7.0运行正常"
    }



@app.get("/search")
def search(keyword:str):

    result=[]

    for item in products:

        if keyword.lower() in item["name"].lower():

            result.append(item)


    return {
        "keyword":keyword,
        "count":len(result),
        "data":result
    }



@app.get("/recommend")
def recommend():

    return sorted(
        products,
        key=lambda x:x["score"],
        reverse=True
    )
