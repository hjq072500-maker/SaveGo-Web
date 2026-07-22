// SaveGo V7.0 AI Shopping Engine


// 商品数据库（V7测试数据）

const products = [

{
name:"iPhone 16 Pro",
category:"手机",
price:7399,
score:92,
platform:[
"淘宝 ¥7399",
"京东 ¥7499",
"亚马逊 ¥7599"
]
},


{
name:"MacBook Air M4",
category:"电脑",
price:8999,
score:95,
platform:[
"苹果官网 ¥8999",
"京东 ¥8899",
"淘宝 ¥8799"
]
},


{
name:"小米15",
category:"手机",
price:3999,
score:88,
platform:[
"小米商城 ¥3999",
"京东 ¥4099",
"淘宝 ¥3899"
]
}

];




// 商品搜索

function search(){


let keyword =
document.getElementById("keyword").value;



let box =
document.getElementById("products");



let result =
products.filter(item=>


item.name.includes(keyword)
||
item.category.includes(keyword)


);



if(result.length===0){


box.innerHTML=`

<div class="card">

<h2>
没有找到商品
</h2>

<p>
AI正在扩大搜索范围...
</p>

</div>

`;

return;

}





box.innerHTML="";



result.forEach(item=>{


box.innerHTML += `


<div class="card">


<h2>
${item.name}
</h2>


<div class="score">

SaveGo评分：
${item.score}

</div>



<div class="price">

¥${item.price}

</div>



<h3>
价格比较
</h3>


${

item.platform.map(
p=>`

<div class="platform">

${p}

</div>

`
).join("")

}



<br>


<button
class="button"
onclick="favorite('${item.name}')">

❤️ 收藏

</button>


</div>


`;

});


}




// 收藏系统


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

name+" 已加入收藏"

);


}




// AI购物助手


function aiRecommend(){



let budget = prompt(

"请输入你的预算，例如：5000"

);



if(!budget){

return;

}




let result;



if(budget>=7000){


result=
"推荐：iPhone 16 Pro 或 MacBook Air M4";


}

else if(budget>=4000){


result=
"推荐：小米15 或 中端旗舰手机";


}

else{


result=
"推荐：高性价比入门产品";


}




alert(

"SaveGo AI分析结果：\n\n"

+result

);



}





// 查看收藏


function showFavorites(){


let data =

JSON.parse(

localStorage.getItem(
"savego_favorites"
)

||
"[]"

);



alert(

"我的收藏：\n"

+
data.join("\n")

);


}
