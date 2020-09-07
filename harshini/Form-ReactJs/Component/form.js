import React, {Component} from 'react';
import { Form, FormGroup, FormFeedback, Label, Input, Button } from 'reactstrap';

class FormDetail extends Component {

    constructor(props){
        super(props);

        this.state = this.getInitialState();
    }

    getInitialState = () => ({
        data: {
            name: '',
            number: '',
            dept: '',
            sem: ''
        }         
    });

    handleSubmit = (e) => {
        e.preventDefault();
        const { data } = this.state;

        console.log(data);
        this.setState(this.getInitialState());
    }

    handleChange = (e) =>{
        this.setState({
            data:{
                ...this.state.data,
                [e.target.name]: e.target.value
            }
        });

    }
    render()
    {
        const {data} = this.state;
        return (
            <Form onSubmit= {this.handleSubmit}>
                <FormGroup>
                    <Label for = "name">Name</Label>
                        <Input id="name" value={data.name} placeholder="Enter your Name" name="name" onChange={this.handleChange}></Input>
                </FormGroup>

                <FormGroup>
                    <Label for = "number">Register Number</Label>
                    <Input id="number" type="number" value={data.number} placeholder="Enter valid Number" name="number" onChange={this.handleChange}></Input>
                </FormGroup>

                <FormGroup>
                    <Label for = "dept">Department</Label>
                    <Input id="dept" name="dept"value={data.dept}placeholder="Deparment ID" onChange={this.handleChange}></Input>
                </FormGroup>

                <FormGroup>
                    <Label for = "sem">Semester</Label>
                    <Input id="sem" type ="number" placeholder="Enter Number" name="sem" value={data.sem} onChange={this.handleChange} ></Input>
                </FormGroup>

                <Button color ="danger">
                    Submit
                </Button>
            </Form>
        );
    }
}

export default FormDetail;