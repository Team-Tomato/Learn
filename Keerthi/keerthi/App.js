import React,{Component} from 'react';
import './App.css';
import BarChart from './BarChart';

const w = 500;
const h = 400;

class Fetch extends Component {
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
    <h4 className = "heading" style = {{alignItems:"center"}}>Barchart for commit count</h4>
      {this.state.fetch ?(
          <div>
            <BarChart data = {this.state.commit} info = {this.state.login} w={w} h={h} color="pink"></BarChart> 
                   <br/>
              </div>  
      ):
      (<div>
       
        </div>   )
}
      ):

      }
      </div>
);
}
}
export default Fetch;