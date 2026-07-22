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
// =======================
// 用户注册
// =======================


async function register(){


let username =
document.getElementById(
"username"
).value;


let password =
document.getElementById(
"password"
).value;



let res =
await fetch(
API+"/register",
{

method:"POST",

headers:{
"Content-Type":
"application/json"
},


body:JSON.stringify({

username,

password

})

});


let data =
await res.json();


alert(
data.success
?
"注册成功"
:
"注册失败"
);


}



// =======================
// 用户登录
// =======================


async function login(){


let username =
document.getElementById(
"username"
).value;


let password =
document.getElementById(
"password"
).value;



let res =
await fetch(
API+"/login",
{

method:"POST",

headers:{
"Content-Type":
"application/json"
},


body:JSON.stringify({

username,

password

})

});


let data =
await res.json();



if(data.login){


localStorage.setItem(
"username",
username
);


location.href=
"user.html";


}

else{


alert(
"账号或密码错误"
);

}


}





// =======================
// 收藏列表
// =======================


async function loadFavorites(){


let username =
localStorage.getItem(
"username"
);



let res =
await fetch(

API+
"/favorites/"
+
username

);



let data =
await res.json();



document.getElementById(
"favorites"
).innerHTML=


data.favorites
.map(

item=>

`
<div class="card">

<h3>
${item}
</h3>

</div>

`

)

.join("");

}
