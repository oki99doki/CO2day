import { useEffect, useState  } from 'react'
import { NavLink } from 'react-router-dom'
//import ProjectListItem from './ProjectListItem'
//import GraphComponent from './GraphComponent'

//import UserListItem from './UserListItem'

// SK: added on 9/30 - for plotting data and creating graphs
//import GraphComponent from './GraphComponent'
import Plot from 'react-plotly.js'
//import GraphComponent from './GraphComponent'

function HomePage() {

  const [ users, setUsers ] = useState([])
  const [ graphData, setGraphData] = useState(null);

  useEffect(() => {
    loadUsers()
  }, []) 

  const loadUsers = () => {
    //fetch('http://localhost:4000/users')
    fetch('http://127.0.0.1:5555/users')
    .then(res => res.json())
    .then(data => {
      setUsers(data.users);
      //console.log(data);
      //console.log(data)
      setGraphData(JSON.parse(data.graph));
      //setGraphData(JSON.parse(data.graph));
    
    })
  }


  // Prepare data for the bar plot
  const prepareGraphData1 = () => {
    const userNames = users.map(user => user.name);
    const electricityData = users.map(user => user.co2Produced_electricity);
    const gasData = users.map(user => user.co2Produced_gas);
    const gasolineData = users.map(user => user.co2Produced_gasoline);
    const flightData = users.map(user => user.co2Produced_flight);


    return [{
      x: userNames,
      y: electricityData,
      name: 'Electricity',
      type: 'bar',
    }, {
      x: userNames,
      y: gasData,
      name: 'Gas',
      type: 'bar',
    }, {
      x: userNames,
      y: gasolineData,
      name: 'Gasoline',
      type: 'bar',
    }, {
      x: userNames,
      y: flightData,
      name: 'Flights',
      type: 'bar',
    }];
  };


  // Prepare data for pie charts
  const prepareGraphData2 = () => {
    return users.map(user => {
      const totalCO2 = user.co2Produced_electricity + user.co2Produced_gas + user.co2Produced_gasoline + user.co2Produced_flight;

      return {
        values: [
          user.co2Produced_electricity,
          user.co2Produced_gas,
          user.co2Produced_gasoline,
          user.co2Produced_flight
        ],
        labels: ['Electricity', 'Gas', 'Gasoline', 'Flights'],
        title: `${user.name} - Total CO2: ${totalCO2.toFixed(1)} kg`,
        totalCO2,
      };
    });
  };




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
        {/* {users.length > 0 ? (
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
        )} */}

        {users.length > 0 && (
          <Plot
            data={prepareGraphData1()}
            layout={{
              title: 'CO2 Emissions by Source',
              barmode: 'group',
              xaxis: {
                title: 'Users',
              },
              yaxis: {
                title: 'CO2 Emissions (kg)',
              },
            }}
          />
        )}
      </div>


      <div>
        <h1>Users and CO2 Emissions</h1>
        {users.length > 0 ? (
          users.map(user => {
            const totalCO2 = user.co2Produced_electricity + user.co2Produced_gas + user.co2Produced_gasoline + user.co2Produced_flight;

            return (
              <div key={user.id} style={{ marginBottom: '40px' }}>
                <h3>{user.name} - Total CO2: {totalCO2.toFixed(1)} kg</h3>
                <Plot
                  data={[
                    {
                      values: [
                        user.co2Produced_electricity,
                        user.co2Produced_gas,
                        user.co2Produced_gasoline,
                        user.co2Produced_flight
                      ],
                      labels: ['Electricity', 'Gas', 'Gasoline', 'Flights'],
                      type: 'pie',
                      hole: 0.4, // If you want a donut chart
                    }
                  ]}
                  layout={{
                    title: `${user.name}'s CO2 Emissions`,
                    showlegend: true,
                    height: 300,
                    width: 300,
                  }}
                />
              </div>
            );
          })
        ) : (
          <p>No users found.</p>
        )}
      </div>



      


    <div>


            {/* <h1>Users and CO2 Emissions</h1>
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
            )} */}


            {/* <GraphComponent/> */}




            {/* {graphData && (
                <Plot
                    data={graphData.data}
                    layout={graphData.layout}
                />
            )} */}

            {/* {graphData ? (
                <Plot
                    data={graphData.data}
                    layout={graphData.layout}
                />
            ) : (
                <p>Loading...</p>
            )} */}


            
                {/* <Plot
                    data={data.data}
                    layout={data.layout}
                /> */}
            

              
        </div>

    

</section>
  )
}

export default HomePage