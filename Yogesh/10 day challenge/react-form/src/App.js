import React, { Component } from 'react';
import { Button, Form, FormGroup, Label, Input } from 'reactstrap';
import { FacebookLoginButton, GithubLoginButton, InstagramLoginButton } from 'react-social-login-buttons';
import './App.css';

class App extends Component {
    render() {
        return (
          <div className='content'>
          <div className='height'>
          </div>
          <Form className = 'login-form form' id='demo'>
            <h3 className = 'text-center'> <span className = 'font-weight-bold'>🍅teamtomato</span>.tech</h3>
            <h4 className = 'text-center'> Welcome </h4>


            <FormGroup>
            <Label> Email </Label>
            <Input type = 'email'  placeholder = 'Enter your email address'/>
            </FormGroup>
            <FormGroup>
            <Label > Password < /Label>
            <Input type = 'password'
            placeholder = 'Password' />
            </FormGroup>

             <Button className = 'btn-block btn-lg btn-block' > Log - in < /Button> <
            div className = 'text-center pt-3 head' > Or
            continue with any social account < /div>
            <FacebookLoginButton / >
            <InstagramLoginButton / >
              </Form>
              </div>
        )
    }
}


export default App;
