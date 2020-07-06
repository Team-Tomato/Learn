import React, {Component, useRef} from 'react';
import * as d3 from "d3";

class BarChart extends Component {
    constructor(props) {
        super(props);
        this.myRef = React.createRef();
}
componentDidMount(){
        let accessToRef = d3.select(this.myRef.current);
        accessToRef.style("background-color","white")
}
drawChart() {
       // const data = [];
       const {data, w, h, color} = this.props;
     //  const el = new Element('div');
       const svg = d3.select(this.myRef.current)
           .append('svg')
           .attr('id', 'chart')
           .attr('width', w)
           .attr('height', h);
      
       const accessToRef = d3.select(this.myRef.current)
        .append("svg")
        .attr("width",w)
        .attr("height",h)
        .style("padding",10)
        .style("margin-left",50);
       const margin = {
               top: 60,
               bottom: 50,
               left: 80,
               right: 40
       };
        const xScale = d3.scaleBand()
        .domain(data.map(d => d.total))
        .range([0,w]);
        const yScale = d3.scaleLinear()
        .domain([0,d3.max(data,d => d.login)])
        .range([h,0]);
        const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

        accessToRef.selectAll("rect")
        .data(data)
        .enter()
        .append("rect")
        .attr("x",(d,i)=>i*70)
        .attr("y",(d,i)=>h-10*d)
        .attr("width",55)
        .attr("height",(d,i)=>d*10)
        .attr("fill","pink")

        accessToRef.selectAll("text")
        .data(data)
        .enter()
        .append("text")
        .text((d) => d)
        .attr("x",(d,i) => i*70)
        .attr("y",(d,i) => h-(10*d)-3)

        accessToRef.selectAll('.bar-label')
    .data(data)
    .enter()
    .append('text')
    .classed('bar-label', true)
    .attr('x', d => xScale(d.country) + xScale.bandwidth()/2)
    .attr('dx', 0)
    .attr('y', d => yScale(d.value))
    .attr('dy', -6)
    .text(d => d.value);

    const xAxis = d3.axisBottom()
    .scale(xScale);
    
        accessToRef.append('g')
    .classed('x axis', true)
    .attr('transform', `translate(0,${h})`)
    .call(xAxis);

    const yAxis = d3.axisLeft()
    .ticks(5)
    .scale(yScale);

        accessToRef.append('g')
    .classed('y axis', true)
    .attr('transform', 'translate(0,0)')
    .call(yAxis);

        accessToRef.select('.x.axis')
    .append('text')
    .attr('x',  w/2)
    .attr('y', 60)
    .attr('fill', '#000')
    .style('font-size', '20px')
    .style('text-anchor', 'middle')
    .text('Contibutors');

        accessToRef.select('.y.axis')
    .append('text')
    .attr('x', 0)
    .attr('y', 0)
    .attr('transform', `translate(-50, ${h/2}) rotate(-90)`)
    .attr('fill', '#000')
    .style('font-size', '20px')
    .style('text-anchor', 'middle')
    .text('Commit Count');
    }

    componentDidMount() {
        this.drawChart();
    }
    render(){
      return <div ref={this.myRef}></div>
    }

        
      }

export default BarChart;