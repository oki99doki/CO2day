import { useState, useEffect } from 'react'
import UserList from './UserList'

//import Plot from 'react-plotly.js';

function UserPage() {

  const [ users, setUsers ] = useState([])
  const [ graphData, setGraphData ] = useState(null);

  useEffect(() => {
    loadUsers()
  }, []) 

  const loadUsers = () => {
    //fetch('http://localhost:4000/users')
    fetch('http://127.0.0.1:5555/users')
    .then(res => res.json())
    .then(data => {
      console.log(data); // Log the raw response
      setUsers(data.users);
      //setGraphData(JSON.parse(data.graph)); // Parse the graph data
    })
    .catch(error => console.error('Error fetching data:', error));

  }

  return (
    <section>
      {/* <div style={{ margin: "60px 0" }}> */}
      <div style={{ margin: "0px 0" }}>
          <h1>Users</h1> 
            <UserList users={users} />
      </div>

      

    </section>
  )
}

export default UserPage