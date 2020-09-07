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
                        <Input id="name" value={data.name} invalid={false} name="name" onChange={this.handleChange}></Input>
                    <FormFeedback>Please Fill this out  </FormFeedback>
                </FormGroup>

                <FormGroup>
                    <Label for = "number">Register Number</Label>
                    <Input id="number" type="number" value={data.number} invalid={false} name="number" onChange={this.handleChange}></Input>
                    <FormFeedback>Enter valid Number </FormFeedback>
                </FormGroup>

                <FormGroup>
                    <Label for = "dept">Department</Label>
                    <Input id="dept" invalid={false} name="dept"value={data.dept} onChange={this.handleChange}></Input>
                    <FormFeedback>Please Fill this out  </FormFeedback>
                </FormGroup>

                <FormGroup>
                    <Label for = "sem">Semester</Label>
                    <Input id="sem" type ="number" invalid={false} name="sem" value={data.sem} onChange={this.handleChange} ></Input>
                    <FormFeedback>Enter valid number  </FormFeedback>
                </FormGroup>

                <Button color ="danger">
                    Submit
                </Button>
            </Form>
        );
    }
}

export default FormDetail;