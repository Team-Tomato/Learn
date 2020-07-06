import React, { Component } from 'react';
import './style.css';

import axios from 'axios';
class App extends Component {
    constructor(props) {
        super(props);
        this.state = { articles: [] };
        this.componentDidMount = this.componentDidMount.bind(this)
    }

    componentDidMount() {
        axios.get(`https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=a67eef8277874660b267055a074d0de8`)
            .then(res => {
                this.setState({
                    articles: res.data.articles
                });
            });
    }
    render() {
        return ( < div >
            <
            div className = "form" >
            <
            h1 > Top News from BBC < /h1> < /
            div > <
            div className = "App" > {
                this.state.articles.map((item, index) => {
                    return ( <
                        div className = "Contents" >

                        <
                        div >
                        <
                        img className = "image"
                        src = { item.urlToImage }
                        alt = " " /
                        >
                        <
                        /div>

                        <
                        h2 className = "title" > { item.title } < /h2> <
                        p className = "description" > { item.description } < /p> <
                        p className = "source" > Source: { item.source.name } < /p> <
                        a href = { item.url }
                        className = "url" > Read More.. < /a> <hr/ > <
                        /div> 
                    )
                })
            } <
            /div> <
            /div>


        )
    }
}
export default App