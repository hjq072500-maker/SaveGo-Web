// SaveGo V6.3 Interactive Engine

const products=[
{
name:"iPhone 16 Pro",
price:7499,
score:92
},
{
name:"MacBook Air M4",
price:8999,
score:95
},
{
name:"小米15",
price:3999,
score:88
}
];


function searchProduct(){

let input=document.querySelector("#searchInput").value;

let result=document.querySelector("#result");

let data=products.filter(
p=>p.name.includes(input)
);


if(data.length===0){

result.innerHTML="没有找到商品";

return;

}


result.innerHTML=data.map(
p=>`

<div class="card">

<h2>${p.name}</h2>

<p>SaveGo评分:${p.score}</p>

<div class="price">
¥${p.price}
</div>

<button onclick="favorite('${p.name}')">
❤️ 收藏
</button>

</div>

`
).join("");

}



function favorite(name){

let list=
JSON.parse(
localStorage.getItem("favorites")
||"[]"
);


list.push(name);


localStorage.setItem(
"favorites",
JSON.stringify(list)
);


alert(
name+" 已收藏"
);

}




function aiRecommend(){

alert(
"AI分析完成：根据预算和需求推荐最佳商品"
);

}
