import React, { useState } from "react";

import "./App.css";
import { Button, Form, FormGroup, Label, Input } from "reactstrap";

const App = () => {
  const [mail, setMail] = useState("");
  const Handlemail = (event) => {
    setMail(event.currentTarget.value);
    console.log(mail);
  };

  const [pass, setPass] = useState("");
  const Handlepass = (event) => {
    setPass(event.currentTarget.value);
    console.log(pass);
  };

  function Clicked() {
    if (mail === "" && pass === "") {
      alert("Enter Email and Password");
    }
  }

  return (
    <div className="container-fluid">
      <div className="row">
        <div className="col"></div>
        <div className="col box">
          <h1>Login Form </h1>
          <Form>
            <FormGroup>
              <Label for="Email">Email</Label>
              <Input
                onChange={Handlemail}
                type="email"
                name="email"
                id="email"
                className="email"
                placeholder="Enter your email"
                class="form-control"
              />
            </FormGroup>
            <FormGroup>
              <Label for="examplePassword">Password</Label>
              <Input
                onChange={Handlepass}
                type="password"
                id="pass"
                name="password"
                className="password"
                placeholder="Enter your password"
                class="form-control"
              />
            </FormGroup>
            <FormGroup check>
              <Label check>
                <Input type="checkbox" />
                Remember me
              </Label>
            </FormGroup>
            <Button
              onClick={Clicked}
              outline
              color="success"
              className="btn-block"
            >
              Submit
            </Button>
          </Form>
        </div>
        <div className="col"></div>
      </div>
    </div>
  );
};

export default App;
