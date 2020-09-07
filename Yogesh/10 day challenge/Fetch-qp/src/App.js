import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './App.css';

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            loading: false,
            qp: []
        };
    }

    componentDidMount() {
        const url = "https://teamtomato.herokuapp.com/api/v1/question";
        fetch(url)
            .then(response => {

                return response.json()

            })
            .then((parsedData) => {
                console.log(parsedData);
                this.setState({ qp: parsedData })
            });
    }

    render() {

        var { loading, qp } = this.state;

        return ( <
            div className = "App" > {
                qp.map(data => ( <
                    tr >
                    <
                    td > { data.subjectName } < /td> <
                    td > { data.staff } < /td> <
                    td > { data.year } < /td> <
                    td > < a href = "{ data.subjectName }" > Download < /a></td >
                    <
                    /tr>
                ))
            }; <
            /div>



        )
    }
}





export default App;