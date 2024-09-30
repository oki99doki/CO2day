import { useEffect, useState  } from 'react'
import { NavLink } from 'react-router-dom'
//import ProjectListItem from './ProjectListItem'

import UserListItem from './UserListItem'

// SK: added on 9/30 - for plotting data and creating graphs
//import GraphComponent from './GraphComponent'
import Plot from 'react-plotly.js'

function HomePage() {

  const [ users, setUsers ] = useState([])
  const [graphData, setGraphData] = useState(null);

  useEffect(() => {
    loadUsers()
  }, []) 

  const loadUsers = () => {
    //fetch('http://localhost:4000/users')
    fetch('http://127.0.0.1:5555/users')
    .then(res => res.json())
    .then(data => setUsers(data.users))
  }

  //const [houses, setHouses] = useState([])


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
      
        {/* <GraphComponent/> */}



        {/* console.log(users); */}
        {/* {
          users.map(el => <UserListItem user={el} key={el.id} />)
        } */}

    </div>


    <div>
            <h1>Users and CO2 Emissions</h1>
            {users.length > 0 ? (
                <ul>
                    {users.map(user => (
                        <li key={user.id}>
                            {user.name}<br />
                            CO2 from Electricity: {user.co2Produced_electricity.toFixed(1)} kg<br />
                            CO2 from Gas: {user.co2Produced_gas.toFixed(1)} kg<br />
                            CO2 from Gasoline: {user.co2Produced_gasoline.toFixed(1)} kg<br />
                            CO2 from Flights: {user.co2Produced_flight.toFixed(1)} kg<br />
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No users found.</p>
            )}
            {graphData && (
                <Plot
                    data={graphData.data}
                    layout={graphData.layout}
                />
            )}
        </div>

    

</section>
  )
}

export default HomePage