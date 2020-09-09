import React, { Component } from 'react';
import './App.css';

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
          error: null,
          isLoaded: false,
          data: []
        };
      }
    
      componentDidMount() {
        fetch("https://reqres.in/api/users")
          .then(res => res.json())
          .then(
            (result) => {
              this.setState({
                isLoaded: true,
                data: result.data
              });
            },
            
            (error) => {
              this.setState({
                isLoaded: true,
                error
              });
            }
          )
      }
    
      render() {
        const { error, isLoaded, data } = this.state;
        if (error) {
          return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
          return <div>Loading...</div>;
        } else {
            
          return (
            <div>
                <tr>
                  <td>EMAIL</td> 
                  <td>FIRST NAME</td> 
                  <td>LAST NAME</td>
                </tr>
              {data.map(item => (
                <tr>
                  <td>{item.email}</td> 
                  <td>{item.first_name}</td> 
                  <td>{item.last_name}</td>
                </tr>
              ))}
            </div>
          );
        }
      }
}
export default App;





