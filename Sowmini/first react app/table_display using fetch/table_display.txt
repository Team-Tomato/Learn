import React, { Component } from 'react';  
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
    fetch('https://jsonplaceholder.typicode.com/users')
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
          <h1 align="center">Personal Details</h1>
            <table align="center" border="1">
              <tr>
              <th>Name</th>
              <th>Website</th>
              <th>Phone no</th>
              <th>Email-ID</th>
              <th>City</th>
              </tr>
              {items.map(item=>
                <tr key={item.id}>
                 <td>{item.name}</td> 
                 <td>{item.website}</td>
                 <td>{item.phone}</td>
                 <td>{item.email}</td>
                 <td>{item.address.city}</td>
                </tr>
              )}
            </table>
        </div>        
  ) ; 
  }
} 
}
export default App;
