import React,{Component} from 'react';
import Barchart from './Barchart.js';

const w=800;
const h=500;
class App extends Component {
  constructor(props)
  {
      super(props);
      this.state={ repo: [],
                   commit:[],
                  login:[],
                  fetch:false}
  }
  
async componentDidMount()
{
const url="https://api.github.com/repos/Team-Tomato/QuestionPaper_Frontend/stats/contributors"
const response=await fetch(url);
const output=await response.json();
console.log(output);
this.setState({repo :output});
for (var i = 0; i < this.state.repo.length; i++) {

this.state.commit.push(this.state.repo[i].total)
this.state.login.push(this.state.repo[i].author.login)
}
this.setState({
  fetch:true
})
}

render() {
return (
  <div>
      {this.state.fetch ?(
          <div>
              <Barchart data={this.state.commit} info={this.state.login} w={w} h={h} color="blue"/>
                   <br/>
              </div>
            ):
            (<div>
             </div>)
            }
  </div>
);
}
}
export default App;

