import { useState, useEffect } from 'react'
import UserList from './UserList'

function UsersPage() {
  const [ projects, setUsers ] = useState([])

  useEffect(() => {
    loadUsers()
  }, []) 

  const loadUsers = () => {
    fetch('http://localhost:4000/users')
    .then(res => res.json())
    .then(data => setUsers(data))
  }

  return (
    <div>
      <UserList users={users} />
    </div>
  )
}

export default UsersPage