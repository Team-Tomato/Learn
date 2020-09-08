
import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';
import { Table } from 'react-bootstrap';

const App = () => {
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [items, setItems] = useState([]);
  const url = "https://teamtomato.herokuapp.com/api/v1/question";
  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setItems(result);
        },
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [])
  
  const renderData = (row,index) => {
    return(
      <tr key={index}>
        <td>{row.id}</td>
        <td>{row.shortForm}</td>
        <td>{row.staff}</td>
        <td>{row.subjectName}</td>
        <td>{row.url}</td>
        <td>{row.year}</td>
      </tr>
    )
  }
  return (
    <div className="App">
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Short Form</th>
            <th>Staff</th>
            <th>Subject Name</th>
            <th>URL</th>
            <th>Year</th>
          </tr>
        </thead>
        <tbody>
          {items.map(renderData)}
        </tbody>
      </Table>
    </div>
  );
}

export default App;
