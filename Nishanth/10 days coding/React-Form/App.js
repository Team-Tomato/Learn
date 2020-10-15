import React, { Component } from 'react';
import {
  Container, Col, Form,
  FormGroup, Label, Input,
  Button,
} from 'reactstrap';
import './App.css';


class App extends Component {
  render() {
    return (
      <div className="container">
      <Container className="App">
        <h2 className="heading">Sign Up</h2>
        <Form className="form">
          <Col>
            <FormGroup className="element">
              <Label>Username</Label>
              <Input
              className="input"
                type="text"
                name="user"
                id="Username"
                placeholder="Username"
              />
            </FormGroup>
          </Col>
          <Col>
            <FormGroup className="element">
              <Label>Email</Label>
              <Input
              className="input"
                type="email"
                name="email"
                id="exampleEmail"
                placeholder="Email address"
              />
            </FormGroup>
          </Col>
          <Col>
            <FormGroup className="element">
              <Label for="examplePassword">Password</Label>
              <Input
              className="input"
                type="password"
                name="password"
                id="examplePassword"
                placeholder="New Password"
              />
            </FormGroup>
          </Col>
          <Col>
            <FormGroup className="element">
              <Label for="examplePassword">Confirm Password</Label>
              <Input
              className="input"
                type="password"
                name="password"
                id="examplePassword"
                placeholder="Confirm New password"
              />
            </FormGroup>
          </Col>
          <div className="submit">
          <Button className="btn">Submit</Button>
          </div>
        </Form>
      </Container>
      </div>
      );
  }
}

export default App;