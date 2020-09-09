async function getData()
{
    url = "https://teamtomato.herokuapp.com/api/v1/question";

    var resp = await fetch(url);
    var json = await resp.json();

    let container = document.getElementById("data");
    var tRows = "";
    json.forEach(ele => {
        tRows += "<tr>" 
                +"<td>" + ele["id"] + "</td>"
                +"<td>" + ele["shortForm"] + "</td>"
                +"<td>" + ele["staff"] + "</td>"
                +"<td>" + ele["subjectName"] + "</td>"
                +"<td>" + ele["url"] + "</td>"
                +"<td>" + ele["year"] + "</td>"
                +"<tr>"
    });
    container.innerHTML = tRows;
}

getData();