// =================================
// SaveGo AI V7.0 Frontend API
// =================================


// 后端地址
const API_URL = 
"https://savego-ai-api.onrender.com";



// ================================
// 商品搜索
// ================================

async function searchProduct(){

    const input =
    document.getElementById(
        "keyword"
    );


    const result =
    document.getElementById(
        "result"
    );


    const keyword =
    input.value.trim();


    if(!keyword){

        result.innerHTML =
        "请输入商品名称";

        return;
    }



    result.innerHTML =
    "正在搜索...";



    try{


        const response =
        await fetch(
            API_URL + "/search",
            {

                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },


                body:
                JSON.stringify({

                    keyword:keyword

                })

            }
        );



        const data =
        await response.json();



        let html =
        "<h3>搜索结果</h3>";



        data.products.forEach(
            item=>{


                html += `

                <div class="product">

                <h4>
                ${item.name}
                </h4>


                <p>
                平台:
                ${item.platform}
                </p>


                <p>
                价格:
                ${item.price}
                </p>


                </div>

                `;


            }
        );



        result.innerHTML =
        html;



    }

    catch(error){

        result.innerHTML =
        "服务器连接失败";

        console.log(error);

    }


}





// ================================
// AI助手
// ================================


async function askAI(){


    const box =
    document.getElementById(
        "ai-result"
    );


    box.innerHTML =
    "AI思考中...";



    try{


        const response =
        await fetch(
            API_URL+"/ai"
        );


        const data =
        await response.json();



        box.innerHTML =
        data.reply;



    }

    catch(e){

        box.innerHTML =
        "AI服务连接失败";

    }


}
