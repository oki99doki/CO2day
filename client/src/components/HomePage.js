import { useEffect, useState  } from 'react'
import { NavLink } from 'react-router-dom'
//import ProjectListItem from './ProjectListItem'

import UserListItem from './UserListItem'

function HomePage() {

  const [users, setUsers] = useState([])
  

  //✅ 9. Create homepage with top 5 liked projects.
  useEffect(() => {
    //fetch('http://localhost:4000/projects?_sort=claps&_order=desc&_limit=5')
    fetch('http://127.0.0.1:5555/users')
    //fetch('http://127.0.0.1:5555/users?_sort=id&_limit=5')
    .then(res => res.json())
    
    .then(data => {
      console.log(data);
      setUsers(data);
    });
  }, []);

  return (
    <section className="box">
    <h2>Hey!  Welcome to this CO2 Calculator.</h2>
    <p>
        Looking for an app to show the impact of today’s consumption from sources such as transportation, utilities, etc. 
        on CO2 produced and that based on the user’s input on  can provide an estimate of the amount of annual CO2 produced.
    </p>

    <div style={{ margin: "60px 0" }}>
        <NavLink to={"/users"}>
          <button className="button" >
              View All Users
          </button>
        </NavLink>
        console.log(users);
        {/* {
          users.map(el => <UserListItem user={el} key={el.id} />)
        } */}

    </div>

    

</section>
  )
}

export default HomePage