import React,{useState,useEffect} from 'react';
import axios from 'axios'
import './App.css';

function App() {
  const [data, setData] = useState([])
  useEffect(() => {
      axios.get("https://teamtomato.herokuapp.com/api/v1/question")
      .then(res=>{setData(res.data)} )
      .catch(err=>console.log(err))  
  }, [])
  return (
      <>
     
      <div className="container">
            <table>
            <thead>
              <th>S.No</th>
              <th>Id</th>
              <th>Staff_Name</th>
              <th>Subject_Name</th>
              <th>Url</th>
              <th>Year</th>
            </thead>
          {data.map((details,index)=>
          <tbody key={index}>
            <tr>
           <td>{index}</td>
           <td>{details.id}</td>
           <td>{details.staff}</td>
           <td>{details.subjectName}</td>
           <td>{details.url}</td>
           <td>{details.year}</td>
            </tr>
            </tbody>
            )}
            </table>      
      </div>    
      </>
  )
}


export default App;
