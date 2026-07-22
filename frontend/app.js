const API =
"http://localhost:10000";



async function searchAI(){


let keyword =
document.getElementById(
"keyword"
).value;



let budget =
document.getElementById(
"budget"
).value;



let response =
await fetch(
API+"/recommend",
{

method:"POST",

headers:{
"Content-Type":
"application/json"
},


body:
JSON.stringify({

keyword:keyword,

budget:Number(budget)

})

}

);



let data =
await response.json();



showResult(data);



}




function showResult(data){


let box =
document.getElementById(
"result"
);



box.innerHTML="";



data.recommendation
.forEach(item=>{


box.innerHTML += `


<div class="card">


<h2>
${item.name}
</h2>


<p>
价格：
${item.price}
</p>


<p>
平台：
${item.platform}
</p>


<p>
评分：
${item.score}
</p>


<p>
${item.reason}
</p>


</div>


`;


});


}
