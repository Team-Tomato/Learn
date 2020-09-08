import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { Button, Form, FormGroup, Label, Input, FormText } from 'reactstrap';


function App() {
    return (
      <div className="container-fluid">
<div className="row">
<div className="col"></div>
<div className="col box">
<h1>Login Form </h1>
      <Form>
      <FormGroup>
        <Label for="Email">Email</Label>
        <Input type="email" name="email" className="email" placeholder="Enter your email" />
      </FormGroup>
      <FormGroup>
        <Label for="examplePassword">Password</Label>
        <Input type="password" name="password" className="password" placeholder="Enter your password" />
      </FormGroup>
      <FormGroup check>
      <Label check>
      <Input type="checkbox" />
      Remember me

      </Label>
</FormGroup>
      <Button outline color="success" className="btn-block">Submit</Button>

</Form>
</div>
<div className="col"></div>
</div>
</div>
    );
}

export default App;
