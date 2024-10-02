import React, { useState, useEffect } from 'react';

function EditFlight({ flight, onUpdate }) {
  const [editedFlight, setEditedFlight] = useState(flight);

  useEffect(() => {
    setEditedFlight(flight);
  }, [flight]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setEditedFlight({
      ...editedFlight,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch(`http://127.0.0.1:5555/flights/${flight.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(editedFlight),
    });
    onUpdate(); // Refresh the flight list
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="name" value={editedFlight.name} onChange={handleChange} required />
      <input type="text" name="departure" value={editedFlight.departure} onChange={handleChange} required />
      <input type="text" name="destination" value={editedFlight.destination} onChange={handleChange} required />
      <label>
        International:
        <input type="checkbox" name="international" checked={editedFlight.international} onChange={handleChange} />
      </label>
      <input type="number" name="distance" value={editedFlight.distance} onChange={handleChange} required />
      <button type="submit">Update Flight</button>
    </form>
  );
}

export default EditFlight;