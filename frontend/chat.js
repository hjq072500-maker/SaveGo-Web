const API =
"http://localhost:10000";





async function sendMessage(){



let msg =
document.getElementById(
"message"
).value;



let chat =
document.getElementById(
"chat"
);



chat.innerHTML += `

<div class="card">

<b>
你：
</b>

${msg}

</div>

`;



let budget = 10000;



// 简单预算识别

let numbers =
msg.match(/\d+/);


if(numbers){

budget =
Number(numbers[0]);

}




let keyword="";



if(
msg.includes("手机")
){

keyword="手机";

}

else if(
msg.includes("电脑")
){

keyword="电脑";

}

else{

keyword="商品";

}




let res =
await fetch(

API+
"/recommend",

{

method:"POST",

headers:{

"Content-Type":
"application/json"

},

body:JSON.stringify({

keyword:keyword,

budget:budget

})

}

);



let data =
await res.json();



let result =
data.recommendation[0];



chat.innerHTML += `

<div class="card">


<b>
SaveGo AI：
</b>


<br>


推荐：

${result.name}


<br>


价格：

${result.price}


<br>


平台：

${result.platform}


<br>


评分：

${result.score}


<br>


建议：

适合你的预算和需求


</div>


`;



}
