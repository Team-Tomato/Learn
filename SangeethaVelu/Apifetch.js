import React, { Component } from 'react';  
import "./App.css"
class App extends Component{
  constructor(){
    super();
    this.state={
      items:[],
      isLoaded:false,
    }
  }
  componentDidMount()
  {
    fetch('https://teamtomato.herokuapp.com/api/v1/question')
       .then(res => res.json())
       .then(json => {
           this.setState({
             isLoaded: true,
             items: json,
           })
          });
      
  }
  render() {
    var {isLoaded, items}= this.state;
    if(!isLoaded){
        return <div>Loading....</div>;
    }
    else{
       return (  
        <div>  
          <h1 align="center">Fetch api</h1>
              <tr>
              <th>id</th>
              <th>shortForm</th>
              <th>staff</th>
              <th>subjectName</th>
              <th>url</th>
              <th>year</th>
              </tr>
              {items.map(item=>
                <tr key={item.id}>
                 <td>{item.id}</td> 
                 <td>{item.shortForm}</td>
                 <td>{item.staff}</td>
                 <td>{item.subjectName}</td>
                 <td>{item.url}</td>
                 <td>{item.year}</td>
                </tr>
              )}
          
        </div>        
  ) ; 
  }
} 
}
export default App;