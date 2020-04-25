import React, { Component } from 'react';

const API = 'http://dummy.restapiexample.com/api/v1/employees';
//const DEFAULT_QUERY = 'redux';
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      hits: [],
    };
  }
  componentDidMount() {
    fetch(API)
      .then(response => response.json())
      .then(output => this.setState({ hits: output.data }));
  }

  render() {
    console.log( this.state.hits)
        return  (
           
          
          <div>
            { this.state.hits.map((person,index) => (
              <div key={index}>
                Id: {person.id} <br/>
                Employee Name: {person.employee_name}<br/>
                salary : {person.employee_salary} <br/>
                Age : { person.employee_age} <br/>
                <br/>
                </div>
            ))
            }
            
            
          
           </div>
        );
} 
  }

          

export default App;


  

