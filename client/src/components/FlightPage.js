import { useEffect, useState  } from 'react'
import { NavLink } from 'react-router-dom'

import FlightList from './FlightList'
import CreateFlight from './CreateFlight'; // Create this component
import EditFlight from './EditFlight'; // Create this component

function FlightPage() {

  const [ flights, setFlights ] = useState([])
  const [users, setUsers] = useState([]);
  const [aircrafts, setAircrafts] = useState([]);
  const [editingFlight, setEditingFlight] = useState(null);

  useEffect(() => {
    loadFlights();
    loadUsers();
    loadAircrafts();
  }, []) 

  // const loadFlights = () => {
  //   fetch('http://127.0.0.1:5555/flights')
  //   .then(res => res.json())
  //   .then(data => setFlights(data.flights))
  // }

  const loadFlights = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5555/flights');
      const data = await response.json();
      setFlights(data.flights);
    } catch (error) {
      console.error("Error fetching flights:", error);
    }
  };

  const loadUsers = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5555/users');
      const data = await response.json();
      setUsers(data.users);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  const loadAircrafts = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5555/aircrafts');
      const data = await response.json();
      setAircrafts(data.aircrafts);
    } catch (error) {
      console.error("Error fetching aircrafts:", error);
    }
  };

  const handleDelete = async (id) => {
    try {
      await fetch(`http://127.0.0.1:5555/flights/${id}`, { method: 'DELETE' });
      setFlights(flights.filter(flight => flight.id !== id));
    } catch (error) {
      console.error("Error deleting flight:", error);
    }
  };

  const handleEdit = (flight) => {
    setEditingFlight(flight);
  };

  const handleCreateOrUpdate = () => {
    setEditingFlight(null); // Clear editing state after create/update
    loadFlights(); // Reload flights to reflect changes
  };

  
 
  return (
    <section>
      <h1>Flights</h1>
      <FlightList flights={flights} onDelete={handleDelete} onEdit={handleEdit} />
      <CreateFlight users={users} aircrafts={aircrafts} onCreate={handleCreateOrUpdate} />
      {editingFlight && (
        <EditFlight flight={editingFlight} users={users} aircrafts={aircrafts} onUpdate={handleCreateOrUpdate} />
      )}
    </section>
  );
}

export default FlightPage