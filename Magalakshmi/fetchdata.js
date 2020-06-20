
fetch("http://teamtomato.herokuapp.com/api/v1/question").then
(res=>{
  res.json().then(
    data=>{
      console.log(data);
      if(data.length>0)
      {
        var temp = "";

        

data.forEach((u)=>
{
temp +="<tr>";
temp +="<td>"+u.id+"</td>";
temp +="<td>"+u.shortForm+"</td>";
temp +="<td>"+u.staff+"</td>";
temp +="<td>"+u.subjectName+"</td>";
temp +="<td>"+u.url+"</td>";
temp +="<td>"+u.year+"</td></tr>";
})
        document.getElementById("data").innerHTML = temp;
      }
    }
  )
})
