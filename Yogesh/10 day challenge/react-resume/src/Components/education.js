import React, {Component} from 'react';
import { Col, Container, Form, Row } from 'reactstrap';

import {Card} from 'react-bootstrap';


class Education extends Component{

    render(){
        return(
            
           <Row>
               <Col>
               <Card style={{ width: '18rem' }}>
                <Card.Img variant="top" src="holder.js/100px180" />
                <Card.Body>
                    <Card.Title>Card Title</Card.Title>
                    <Card.Text>
                    Some quick example text to build on the card title and make up the bulk of
                    the card's content.
                    </Card.Text>
                    
                </Card.Body>
                </Card>
                </Col>

                <Col>
                <Card style={{ width: '18rem' }}>
                <Card.Img variant="top" src="holder.js/100px180" />
                <Card.Body>
                    <Card.Title>Card Title</Card.Title>
                    <Card.Text>
                    Some quick example text to build on the card title and make up the bulk of
                    the card's content.
                    </Card.Text>
                    
                </Card.Body>
                </Card>
                </Col>
           </Row>

        );
    }


}

export default Education;