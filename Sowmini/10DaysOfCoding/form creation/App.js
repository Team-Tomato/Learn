import React from 'react';  
import './App.css';  
import { Container, Col, Form, Row, FormGroup, Label, Input, Button } from 'reactstrap';  
  
function App() {  
  
  return (  
    <Container className="App">  
  
      <h2 className="PageHeading">Registration Form</h2>  
      <Form className="form">  
        <Col>  
          <FormGroup row>  
            <Label for="name" sm={2}>Name</Label>  
            <Col sm={7}>  
              <Input type="text" id="name" placeholder="Enter first&last name" />  
            </Col>  
          </FormGroup>
          <FormGroup row>
             <Label for="gender" sm={2}>Gender</Label>
             <Col sm={3}>
             <Input type="select" id="gender" placeholder="Choose gender">
                 <option>Male</option>
                 <option>Female</option>
              </Input>
              </Col>
              <Label for="dob" sm={2}>DOB</Label>
              <Col sm={3}>
                <Input typ="date" id="dob" placeholder="month-date-year"/>
              </Col>
          </FormGroup> 
          <FormGroup row>  
            <Label for="Password" sm={2}>Address</Label>  
            <Col sm={8}>  
              <Input type="text" id="address" placeholder="Enter address" />  
            </Col>  
          </FormGroup>  
          <FormGroup row>  
            <Label for="college" sm={2}>College Name</Label>  
            <Col sm={8}>  
              <Input type="text" id="Address" placeholder="Enter your college name" />  
            </Col>  
          </FormGroup>
          <FormGroup row>
            <Label for="ph.no" sm={2}>Mobile.no</Label>
            <Col sm={5}>
              <Input type="tel" id="ph.no" placeholder="+91" /> 
            </Col>
          </FormGroup>     
          <FormGroup row>  
            <Col sm={12}>  
              <Button color="success">Submit</Button>  
            </Col>   
          </FormGroup>  
        </Col>  
      </Form>  
    </Container>  
  );  
}  
  
  
export default App;  