import React,{Component} from 'react';
import { Table } from 'reactstrap';

class tableDisplay extends Component {
  constructor(props) {
    super(props)
    this.state = {
      users: [],
      isLoading: false,
      isError: false
    }
  }

  async componentDidMount(){
    this.setState({isLoading: true})
    const response = await fetch('https://teamtomato.herokuapp.com/api/v1/question')
    if (response.ok) {
      const users = await response.json()
      this.setState({ users, isLoading: false })
    } else {
      this.setState({ isError: true, isLoading: false })
    }
  }

  renderTableHeader = () => {
    return Object.keys(this.state.users[0]).map(attr => <th key={attr}>{attr.toUpperCase()}</th>)
  }
  renderTableRows = () => {
    return this.state.users.map(users => {
      return (
        <tr key={users.id}>
          <td class = "table-secondary">{users.id}</td>
          <td class = "table-info">{users.shortForm}</td>
          <td class = "table-warning">{users.staff}</td>
          <td class = "table-success">{users.subjectName}</td>
          <td class = "table-danger">{users.url}</td>
          <td class = "table-primary">{users.year}</td>
        </tr>

      )
    })
  }

  render(){
    const {users,isLoading,isError} = this.state

    if (isLoading){
      return <div>Loading...</div>
    }
    if(isError){
      return <div>Error...</div>
    }

  return users.length > 0 
  ? (
    <Table responsive="sm" bordered hover class="table">
      <thead class = "thead-dark" >
        <tr>
          {this.renderTableHeader()}
        </tr>
      </thead>
      <tbody>
        {this.renderTableRows()}
      </tbody>
    </Table>
  ):(
    <div>
      No users.
  </div>
  )
  }
}

export default tableDisplay