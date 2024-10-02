import React, { useState } from 'react';

function CreateFlight({ onCreate }) {
  const [flight, setFlight] = useState({
    name: '',
    departure: '',
    destination: '',
    international: false,
    distance: 0,
    user_id: '', // Adjust as necessary
    aircraft_id: '' // Adjust as necessary
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFlight({
      ...flight,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch('http://127.0.0.1:5555/flights', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(flight),
    });
    onCreate(); // Callback to refresh flight list
    setFlight({ name: '', departure: '', destination: '', international: false, distance: 0, user_id: '', aircraft_id: '' }); // Reset form
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="name" value={flight.name} onChange={handleChange} placeholder="Flight Name" required />
      <input type="text" name="departure" value={flight.departure} onChange={handleChange} placeholder="Departure" required />
      <input type="text" name="destination" value={flight.destination} onChange={handleChange} placeholder="Destination" required />
      <label>
        International:
        <input type="checkbox" name="international" checked={flight.international} onChange={handleChange} />
      </label>
      <input type="number" name="distance" value={flight.distance} onChange={handleChange} placeholder="Distance" required />
      <button type="submit">Create Flight</button>
    </form>
  );
}

export default CreateFlight;