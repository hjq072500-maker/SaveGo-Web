# SaveGo AI V7.1
# 商品数据接口层


def search_products(keyword):

    """
    商品搜索接口
    后续可以连接:
    京东API
    淘宝开放平台
    亚马逊API
    """

    products = [

        {
            "name": keyword,
            "platform": "京东",
            "price": 6999,
            "score": 92
        },

        {
            "name": keyword,
            "platform": "淘宝",
            "price": 7199,
            "score": 88
        },

        {
            "name": keyword,
            "platform": "拼多多",
            "price": 6899,
            "score": 90
        }

    ]


    return products



def analyze_products(products):

    """
    AI评分模块
    """

    # 按价格排序

    products.sort(
        key=lambda x:x["price"]
    )


    best = products[0]


    return {

        "best_choice":best,

        "all_products":products,

        "advice":
        "综合价格和评分，推荐最低价商品"

    }
