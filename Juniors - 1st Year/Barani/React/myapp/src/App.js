import React,{Component} from 'react'

class Table extends Component {
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
          <td>{users.id}</td>
          <td>{users.shortForm}</td>
          <td>{users.staff}</td>
          <td>{users.subjectName}</td>
          <td>{users.url}</td>
          <td>{users.year}</td>
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
    <table>
      <thead>
        <tr>
          {this.renderTableHeader()}
        </tr>
      </thead>
      <tbody>
        {this.renderTableRows()}
      </tbody>
    </table>
  ):(
    <div>
      No users.
  </div>
  )
  }
}

export default Table