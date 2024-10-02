import { useEffect, useState  } from 'react'
import { NavLink } from 'react-router-dom'
//import ProjectListItem from './ProjectListItem'

import FlightList from './FlightList'

function FlightPage() {

  const [ flights, setFlights ] = useState([])
  // const [editingFlight, setEditingFlight] = useState(null);

  useEffect(() => {
    loadFlights()
  }, []) 

  const loadFlights = () => {
    fetch('http://127.0.0.1:5555/flights')
    .then(res => res.json())
    .then(data => setFlights(data.flights))
  }

  const handleDelete = async (id) => {
    await fetch(`http://127.0.0.1:5555/flights/${id}`, { method: 'DELETE' });
    setFlights(flights.filter(flight => flight.id !== id));
  };

  // const handleEdit = (flight) => {
  //   setEditingFlight(flight);
  // };

  // const handleCreateOrUpdate = () => {
  //   setEditingFlight(null); // Clear editing state after create/update
  //   loadFlights(); // Reload flights to reflect changes
  // };

  
 
  return (
    // <section className="box">
    <section>
    {/* <h2>Hey!  Welcome to this CO2 Calculator.</h2>
    <p>
        Looking for an app to show the impact of today’s consumption from sources such as transportation, utilities, etc. 
        on CO2 produced and that based on the user’s input on  can provide an estimate of the amount of annual CO2 produced.
    </p> */}

    {/* <div style={{ margin: "60px 0" }}> */}
    <div style={{ margin: "0px 0" }}>

      {/* <HouseList houses={houses} /> */}
      <h1>Flights</h1>
      {/* <FlightList flights={flights} /> */}
      <FlightList flights={flights} onDelete={handleDelete} onEdit={handleEdit} />


  
        {/* console.log(houses); */}
        {/* {
          houses.map(el => <HouseList house={el} key={el.id} />)
        } */}

    </div>

    

</section>
  )
}

export default FlightPage