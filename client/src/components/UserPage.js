import { useState, useEffect } from 'react'
import UserList from './UserList'

function UserPage() {
  const [ users, setUsers ] = useState([])

  useEffect(() => {
    loadUsers()
  }, []) 

  const loadUsers = () => {
    //fetch('http://localhost:4000/users')
    fetch('http://127.0.0.1:5555/users')
    .then(res => res.json())
    .then(data => setUsers(data))
  }

  return (
    <div>
      <UserList users={users} />
    </div>
  )
}

export default UserPage