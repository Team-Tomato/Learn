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
            <table align="center" border="1">
              <tr>
                <th>SHORTFORM</th>
                <th>STAFF</th>
                <th>SUBJECTNAME</th>
                <th>URL</th>
                <th>YEAR</th>
              </tr>
              {items.map(item=>
                <tr key={item.id}>
                 <td>{item.shortForm}</td> 
                 <td>{item.staff}</td>
                 <td>{item.subjectName}</td>
                 <td>{item.url}</td>
                 <td>{item.year}</td>
                </tr>
              )}
            </table>
        </div>        
  ) ; 
  }
} 
}
export default App;
