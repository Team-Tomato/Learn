import React, { Component } from "react";
import "./App.css";
import { Button, Form, Label, FormGroup, Input } from 'reactstrap';
class App extends Component {
    render() {
        return (

            <Form className="App">
                <h1 className="text-center">
                    <span className="font-weight-bold">Sign In</span>
                </h1>
                <h2 className="text-center">Welcome</h2>
                <FormGroup>
                    <Label>Name</Label>
                    <Input type="name" placeholder="Name" />

                </FormGroup>
                <FormGroup>
                    <Label>Email</Label>
                    <Input type="email" placeholder="Email" />
                </FormGroup>
                <FormGroup>
                    <Label>Password</Label>
                    <Input type="password" placeholder="Password" />
                </FormGroup>
                <FormGroup>
                    <Label>Phone number (Format: +91-xxxxxxxxxx)</Label>
                    <Input type="phonenumber" placeholder="Phone number" />
                </FormGroup>
                <FormGroup>
                    <Label>Department</Label>
                    <Input type="select" id="department" placeholder="Department">
                        <option defaultValue>Select Department</option>
                        <option>Msc Computer Science</option>
                        <option>Msc Information Technology</option>
                    </Input>
                </FormGroup>
                <Button className="btn-lg btn-dark btn-block">
                    Submit
                </Button>
            </Form >

        );

    }
}
export default App;
