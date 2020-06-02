import React,{Component} from 'react';
import * as d3 from 'd3';

class Bar extends Component{
    constructor(props){
        super(props);
        this.myRef=React.createRef();
    }
componentDidMount()
{
   const {data,info,w,h,color}=this.props;

   var xScale = d3.scaleBand().range ([0, w]),
   yScale = d3.scaleLinear().range ([h, 0]);

    const accessToRef=d3.select(this.myRef.current)
    .append("svg")
    .attr("width",w)
    .attr("height",w)
    .style("padding",10)
    .style("margin-left",200);

    accessToRef.append("text")
       .attr("transform", "translate(100,0)")
       .attr("x", 100)
       .attr("y", 50)
       .attr("font-size", "24px")
       .text("Commit count for front end repo");

   xScale.domain(info);
   yScale.domain([0,d3.max(data)]);

        accessToRef.append("g")
         .attr("transform", "translate(25," + h + ")")
         .call(d3.axisBottom(xScale))
         .append("text")
         .attr("y", 50)
         .attr("x", 400)
         .attr("fill", "black")
         .attr("font-size","20px")
         .text("Contributors");

        accessToRef.append("g")
        .attr("transform", "translate(40,10)")
        .call(d3.axisLeft(yScale))
        .append("text")
        .attr("x",-170)
        .attr("y", -25)
        .attr("transform", "rotate(-90)")
        .attr("font-size","20px")
        .attr("fill", "black")
        .text("Commit count");
        

         
        accessToRef.selectAll("rect")
         .data(data)
         .enter()
         .append("rect")
         .attr("transform", "translate(80,0)")
         .attr("fill", color)
         .attr("x",(d,i)=>i*128)
         .attr("y",(d,i)=>h-60*d)
         .attr("width", 45)
         .attr("height",(d,i)=> d*60);
}
render()
{
    return <div ref={this.myRef}></div>
}
}
export default Bar;