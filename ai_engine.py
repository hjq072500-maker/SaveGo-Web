# =================================
# SaveGo AI V7.4
# AI Decision Engine
# =================================


def analyze_product(product):


    price = product.get(
        "price",
        0
    )


    name = product.get(
        "name",
        ""
    )


    platform = product.get(
        "platform",
        ""
    )


    # 简单评分模型

    score = 80



    if price < 8000:

        score += 10


    if "Pro" in name:

        score += 5



    if "官方" in platform:

        score += 3



    if score > 100:

        score = 100



    if score >= 90:

        level = "强烈推荐"

        reason = "价格合理，配置和购买价值较高"


    elif score >=80:

        level = "推荐"

        reason = "综合表现不错，可以考虑"


    else:

        level = "谨慎购买"

        reason = "建议等待优惠或比较其他型号"



    return {


        "product": name,

        "platform": platform,

        "score": score,

        "level": level,

        "reason": reason


    }





def generate_advice(products):


    results=[]


    for product in products:


        results.append(

            analyze_product(product)

        )


    results.sort(

        key=lambda x:x["score"],

        reverse=True

    )


    return results
