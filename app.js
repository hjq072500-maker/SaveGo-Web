// ===================================
// SaveGo AI V7.0 前后端连接系统
// ===================================


// 后端API地址
// 本地测试：
const API_URL = "http://127.0.0.1:8000";


// 如果以后部署服务器，把上面改成：
// const API_URL = "https://你的后端地址";




// ================================
// 商品搜索
// ================================

async function search(){


    let keyword = 
    document.getElementById("keyword").value;



    if(keyword.trim()==""){


        alert("请输入商品名称");

        return;

    }



    let box =
    document.getElementById("products");



    box.innerHTML = `

    <div class="card">

    🔍 正在搜索商品...

    </div>

    `;



    try{


        let response =
        await fetch(
        API_URL +
        "/search?keyword="
        +
        encodeURIComponent(keyword)
        );



        let data =
        await response.json();



        showProducts(data.data);



    }

    catch(error){


        box.innerHTML = `

        <div class="card">

        ❌ 后端连接失败

        <br>

        请检查API服务器是否启动

        </div>

        `;


        console.log(error);


    }



}





// ================================
// 显示商品
// ================================


function showProducts(products){



let box =
document.getElementById("products");



if(!products || products.length===0){


box.innerHTML=`

<div class="card">

没有找到商品

</div>

`;

return;

}




box.innerHTML="";



products.forEach(item=>{


box.innerHTML += `


<div class="card">


<h2>
📱 ${item.name}
</h2>



<div class="score">

SaveGo评分：
${item.score}

</div>



<div class="price">

¥${item.price}

</div>



<p>

平台：

${item.platform}

</p>



<button 
class="button"
onclick="favorite('${item.name}')">

❤️ 收藏

</button>



</div>


`;

});


}






// ================================
// 收藏功能
// ================================


function favorite(name){



let favorites =

JSON.parse(

localStorage.getItem(
"savego_favorites"
)

||

"[]"

);




if(!favorites.includes(name)){


favorites.push(name);


}



localStorage.setItem(

"savego_favorites",

JSON.stringify(favorites)

);



alert(

name+
" 已收藏"

);


}






// ================================
// AI推荐
// ================================


async function aiRecommend(){



try{


let response =

await fetch(

API_URL+
"/recommend"

);



let data =

await response.json();



let text =

"SaveGo AI推荐：\n\n";



data.forEach(item=>{


text +=

item.name
+
" 评分:"
+
item.score
+
"\n";


});



alert(text);



}



catch(error){


alert(

"AI服务暂时无法连接"

);


}


}
