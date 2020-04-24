import React,{Component} from 'react'
class App extends Component{
  constructor(){
    super();
    this.state={
      items:[],
      
    }
  }
    
  componentDidMount(){
    fetch('http://dummy.restapiexample.com/api/v1/employees')
    .then(res => res.json())
    .then (json=>{
      this.setState({
        items:json.data,
      })

    });
  }
  render(){
 
  return(
      <div className="App">
        <h1>Employee Details</h1>
        {this.state.items.map((items,index)=>(
      <div key ={index}>
       <h2>Id:{items.id}</h2> 
        <h3>Name:{items.employee_name}</h3>
        <h3>Salary:{items.employee_salary}</h3>
        <h4>Age:{items.employee_age}</h4>
      </div>
    ))}
      </div>
    );
  }
}

export default App;
