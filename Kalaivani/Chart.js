import React, {Component} from 'react';
import { Bar,Line,Pie,Doughnut } from 'react-chartjs-2';

class Chart extends Component{
    constructor(props){
        super(props);
        this.state={
            chartData:{
                labels:this.props.label,
                datasets: [{
                label: 'Contributors',
                data:this.props.data,
                backgroundColor: [
                'rgb(139, 0, 139)',//1 purple
                'rgb(255,254,79)',//2 lemon
                'rgb(255,165,)',// 3 orange
                'rgb(138,43,226)',// 4 blue violet
                'rgb(0,255,0)',// 5 green
                'rgb(255,0,0)',// 6 red
                'rgb(0,0,255)',// 7 blue
                'rgb(0,189,189)', // 8 light blue
                'rgb(255,0,127)',// 9 rose
                'rgb(201,220,135)',// 10 spring bud
                'rgb(153,102,204)',// 11 amethyst
                'rgb(211,33,45)',//12 amaranth
                'rgb(128,0,0)',//13 maroon
                'rgb(154,205,50)',//14 yellow-green
                'rgb(85,107,47)',//15 olive green 
                'rgb(165,42,42)',//16 brown
                'rgb(218,112,214)',//17 orchid
                'rgb(220,20,60)',//18 crimson
                'rgb(255,0,255)',//19 magenta
                'rgb(0,255,255)',//20 cyan
                'rgb(127,255,0)',//21 chartreuse
                'rgb(0,28,128)',//22 teal
                'rgb(184,115,51)',//23 copper
                'rgb(255,255,0)',//24 yellow
                'rgb(52,205,50)',//25 lime green
                'rgb(255,153,153)',//26 salmon
                'rgb(204,119,34)',//27 ochre
                'rgb(199,211,33)',//28 red violet
                'rgb(230,230,250)',//29 lavender
                'rgb(39,89,45)',//30 emerald
                'rgb(170,69,200)',//31
            ],
            borderColor:'rgb(255,255,255)',
            borderWidth: 1
              }]    
            }
          }
        }
        
    
    static defaultProps={
        displayTitle:true,
        displayLegend:true,
        legendPosition:'right'
    }
    render(){
        return(
            <div className="chart">  
            <h1>Data Visualization</h1>           
               <h2>Bar Chart</h2>
                <Bar
                  data={this.state.chartData}
                  options={{
                  maintainAspectRatio: true,
                  title:{
                      display:this.props.displayTitle,
                      text:'Contributions of contributors',
                      fontSize:25,
                      fontColor:'black',
                  },
                  legend:{
                      display:this.props.displayLegend,
                      position:this.props.legendPosition
                  }
              }}
            />
            <hr/>
            <br />
            <h2>Line Chart</h2>
                <Line
                  data={this.state.chartData}
                  options={{
                  maintainAspectRatio: true,
                  title:{
                      display:this.props.displayTitle,
                      text:'Contributions of Contributors',
                      fontSize:25,
                      fontColor:'black'
                  },
                  legend:{
                      display:this.props.displayLegend,
                      position:this.props.legendPosition
                  }
              }}
            />
            <hr/>
            <br/>
            <h2>Pie Chart</h2>
             <Pie
                  data={this.state.chartData}
                  options={{
                  maintainAspectRatio: true,
                  title:{
                      display:this.props.displayTitle,
                      text:'Contributions of Contributors',
                      fontSize:25,
                      fontColor:'black'
                  },
                  legend:{
                      display:this.props.displayLegend,
                      position:this.props.legendPosition
                  }
              }}
            /> 
            <hr/>
            <br />
            <h2>Doughnut Chart</h2>
            <Doughnut
                  data={this.state.chartData}
                  options={{
                  maintainAspectRatio: true,
                  title:{
                      display:this.props.displayTitle,
                      text:'Contributions of Contributors',
                      fontSize:25,
                      fontColor:'black'
                  },
                  legend:{
                      display:this.props.displayLegend,
                      position:this.props.legendPosition
                  }
              }}
            /> 
            </div>
        )
    }
}
export default Chart;