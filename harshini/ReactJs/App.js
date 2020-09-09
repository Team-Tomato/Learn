import React, { Component } from 'react';
import './App.css';

class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			items: [],
		};
	}
	componentDidMount() {
		const url = 'https://teamtomato.herokuapp.com/api/v1/question';
		fetch(url , {
			method: "GET",
		})
		.then(res => res.json())
		.then(items => {
			this.setState({
				items: items});
		});
	}

	render() {

		var { items} = this.state;

  			return (
    			<div>
    			<h1 align="center">Details</h1>
    			<table align = "center" border ="1">
    			<tr>
    			<th> ID </th>
    			<th> ShortForm </th>
    			<th> Staff </th>
    			<th> Subject </th>
    			</tr>
    			{items.map(item => 
    				<tr key= {item.id}>
    				<td> {item.id} </td>
    				<td> {item.shortForm}</td>
    				<td> {item.staff}</td>
    				<td> {item.subjectName}</td>
    				</tr>
    				)}
    				</table>
      
    			</div>
  		);
	}

}


export default App;
