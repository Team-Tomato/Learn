
async function getapi(url) {
    const response = await fetch(url);
    var data = await response.json();
    console.log(data);
    show(data);
}

getapi("students.json");


function show(data) {
    let tab =  `<tr> 
                <th>NAME</th> 
                <th>ROLL NO</th> 
                <th>SEMESTER</th> 
                <th>CGPA</th> 
                </tr>`; 
    
    for (let r of data.list) { 
        tab += `<tr> 
                <td>${r.name} </td> 
                <td>${r.rollno}</td> 
                <td>${r.semester}</td> 
                <td>${r.cgpa}</td>		 
                </tr>`; 
    }
    document.getElementById("students").innerHTML = tab; 
}