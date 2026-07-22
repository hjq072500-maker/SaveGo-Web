# ==================================
# SaveGo AI Final
# AI Engine
# ==================================


def analyze_product(product):

    score = product["performance"]


    if product["price"] < 5000:

        score += 5


    if score > 100:

        score = 100



    if score >=90:

        level="强烈推荐"

    elif score >=80:

        level="推荐"

    else:

        level="一般"



    return {

        "name":product["name"],

        "price":product["price"],

        "platform":product["platform"],

        "score":score,

        "level":level,

        "reason":
        "综合性能、价格和使用场景分析"

    }




def recommend(products,budget):


    result=[]


    for p in products:

        if p["price"] <= budget:

            result.append(
                analyze_product(p)
            )


    if not result:

        for p in products:

            result.append(
                analyze_product(p)
            )



    result.sort(

        key=lambda x:x["score"],

        reverse=True

    )


    return result
