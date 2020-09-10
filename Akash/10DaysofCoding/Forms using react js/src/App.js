import React from 'react';
import './App.css';
import { Button, Form, FormGroup, Label, Input}
  from 'reactstrap';

function App() {
  return (
    <Form className="forms-app">
     <h1 className="text-center">Create your own account</h1>
     <h3 className="text-center">Enter the below details</h3>
     <FormGroup>
       <Label>First Name</Label>
       <Input type="text" placeholder="Enter your first name"/>
     </FormGroup>
     <FormGroup>
       <Label>Last Name</Label>
       <Input type="text" placeholder="Enter your Last name"/>
     </FormGroup>
     <FormGroup>
       <Label>Email</Label>
       <Input type="email" placeholder="Enter your Email"/>
     </FormGroup>
     <FormGroup>
       <Label>New Password</Label>
       <Input type="password" placeholder="Enter your new password"/>
     </FormGroup>
     <Button class="submit-button" className="btn-lg btn-dark btn-block">
       Submit
     </Button>
    </Form>
  );
}

export default App;
