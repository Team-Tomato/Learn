fetch("https://teamtomato.herokuapp.com/api/v1/question").then(
    response => {
        response.json().then(
            data => {
                console.log(data);
                if (data.length > 0) {
                    var temp = "";

                    data.forEach((obj) => {
                        temp += "<tr>";
                        temp += "<td>" + obj.id + "</td>";
                        temp += "<td>" + obj.shortForm + "</td>";
                        temp += "<td>" + obj.staff + "</td>";
                        temp += "<td>" + obj.subjectName + "</td>";
                        temp += "<td>" + obj.url + "</td>";
                        temp += "<td>" + obj.year + "</td></tr>";

                    })
                    document.getElementById("data").innerHTML = temp;
                }
            }
        )
    }
)