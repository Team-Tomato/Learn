import React, { Component } from 'react';
import { Row,Col,Container } from 'react-bootstrap';
import axios from 'axios';
class NavForm extends Component {
    constructor(props) {
    super(props);
    this.state = {articles: []};   
    this.componentDidMount=this.componentDidMount.bind(this)
    }
    
    componentDidMount() {
        axios.get(`http://newsapi.org/v2/top-headlines?sources=techcrunch&from=2020-05-23&sortBy=publishedAt&apiKey=657c9b0d048543ebbe8da1d5dcf2204d`)
    .then(res => {
            this.setState({
    articles:res.data.articles
            });
    });
    }


    render() {
    return (
        <div>
        <div className="form">
        <h1>Latest News About Techcrunch</h1>
        </div>
        <div className="App">
    {this.state.articles.map((item,index) =>{
        return(
        <div className="Contents">
            <Container>
            <Row>
            <Col className="col-4">
            <img className="image" src={item.urlToImage} />
            </Col>
            <Col className="col-8">
            <h3>{item.title}</h3>
            <b>{item.source.name}</b>
            <p style={{fontSize:'14px'}}>{item.description}</p>
            <a href={item.url} target="__blank" className='btn btn-sm btn-primary search'>Read More</a>
            </Col>
            </Row>
            </Container>
        </div>
    )
})}
</div></div>
)}

}
export default NavForm