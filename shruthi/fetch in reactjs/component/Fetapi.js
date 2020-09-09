import React, { Component } from "react";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";
class Fetapi extends Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
    };
  }
  componentDidMount() {
    const url = "https://jsonplaceholder.typicode.com/users";
    fetch(url, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((items) => {
        this.setState({ items: items });
      });
  }

  render() {
    var { items } = this.state;
    return (
      <div className="App">
        <TableContainer component={Paper}>
          <Table
            className
            align="center"
            size="small"
            aria-label="customized table"
          >
            <h2 align=" Id proof "></h2>
            <TableHead>
              <TableRow>
                <TableCell>ID</TableCell>
                <TableCell align="right">NAME</TableCell>
                <TableCell align="right">USERNAME</TableCell>
                <TableCell align="right">EMAIL</TableCell>
                <TableCell align="right">STREET</TableCell>
                <TableCell align="right">CITY</TableCell>
                <TableCell align="right">CODE</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {items.map((item) => (
                <TableRow key={item.id}>
                  <TableCell component="th" scope="row">
                    {item.id}
                  </TableCell>
                  <TableCell align="right">{item.name} </TableCell>
                  <TableCell align="right">{item.username} </TableCell>
                  <TableCell align="right">{item.email} </TableCell>
                  <TableCell align="right">{item.address.street} </TableCell>
                  <TableCell align="right">{item.address.city} </TableCell>
                  <TableCell align="right">{item.address.zipcode} </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
    );
  }
}
export default Fetapi;
