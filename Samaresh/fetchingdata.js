fetch('https://teamtomato.herokuapp.com/api/v1/question').then(response => response.json()).then(data => {
	for(var i=0;i<data.length;i++){
		document.getElementById("table").innerHTML += 
		`<tr> 
			<td>${data[i].id}</td>
			<td>${data[i].shortForm}</td>			
			<td>${data[i].staff}</td> 
			<td>${data[i].subjectName}</td>
			<td>${data[i].url}</td>
			<td>${data[i].year}</td> 
		</tr>`;
	}
});