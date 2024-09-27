import { useEffect, useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import UserListItem from './UserListItem'

function UserDetails() {
  // ✅ 5b. Use a fetch request in `ProjectDetails` to access a single project.  Use `useParams` to access the id. 
  
  const { id } = useParams()
  const [ user, setUser ] = useState({})
  
  useEffect(() => {
    fetch(`http://localhost:4000/users/${id}`)
    .then(res => res.json())
    .then(data => setUser(data))
  }, [])

  return (
    <div >
      <UserListItem user={user} />
    </div>
  )
}

export default UserDetails