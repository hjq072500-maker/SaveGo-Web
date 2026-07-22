
// SaveGo AI V7.0 Frontend

const API_URL = "https://savego-ai-api.onrender.com";


// 商品搜索
async function searchProduct(){

    let input = document.querySelector("input");

    let keyword = input.value;

    if(!keyword){
        alert("请输入商品");
        return;
    }


    try{

        let res = await fetch(
            API_URL + "/search",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    product:keyword
                })
            }
        );


        let data = await res.json();


        alert(
            "AI分析结果:\n\n"+
            JSON.stringify(data,null,2)
        );


    }catch(error){

        alert(
            "连接服务器失败\n"+
            error
        );

    }

}



// AI助手

async function aiAssistant(){

    try{

        let res = await fetch(
            API_URL+"/ai"
        );


        let data = await res.json();


        alert(
            JSON.stringify(data,null,2)
        );


    }catch(error){

        alert(
            "AI服务连接失败"
        );

    }

}
