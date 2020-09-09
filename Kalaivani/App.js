import React, { Component } from 'react';
import './App.css';
import Chart from './Chart';

class App extends Component {
  constructor(){
    super();
    this.state={repo: null,
      fetched: false,
      contributor: [],
      user: [],
      login: [],
      contributions:[],
    }
  }
  async componentDidMount() {
    var output;
    output = await (await fetch('https://api.github.com/orgs/Team-Tomato/repos')).json()
    this.setState({ repo: output })
    var person;
    for (var i = 0; i < this.state.repo.length; i++) {

      var url = this.state.repo[i].contributors_url
      person = await (await fetch(url)).json()
      this.state.user.push(person)
    }
    for (var i = 0; i < this.state.user.length; i++) {
      for (var j = 0; j < this.state.user[i].length; j++) {
        if (!this.state.login.includes(this.state.user[i][j].login)) {
          this.state.contributor.push(this.state.user[i][j])
          this.state.login.push(this.state.user[i][j].login)
          this.state.contributions.push(this.state.user[i][j].contributions)
        }
      }
    }
    this.setState({ fetched: true })
  }

  render() {
    return (
      <div>
        {this.state.fetched ? (
          <div>
                <Chart label={this.state.login} data={this.state.contributions} />
          </div>) : (<div>
                <h2>Loading...</h2> 
          </div>)
        }
      </div>
    )
  }
}
export default App;
