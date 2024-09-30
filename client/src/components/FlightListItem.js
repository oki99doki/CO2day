// import { FaPencilAlt, FaTrash } from "react-icons/fa";
import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";

// ✅ 5. Update `ProjectListItem`
// ✅ 6. Manage delete project.
function FlightListItem({ flight }) {
	//let { id, name, about, image, claps, link, phase } = user; // TO-DO: adapt this line with corresponding elements on left side
    //let { id, style } = house;
	const navigate = useNavigate();
	
	return (
		        
			<tr flight={flight.id}>
				<td>{flight.id}</td>
				<td>{flight.name}</td>
				<td>{flight.departure}</td>
				<td>{flight.destination}</td>
				<td>{flight.international ? 'Yes' : 'No'}</td>
				<td>{flight.distance} mi</td>
				<td>{flight.co2Produced.toFixed(1)} kg</td>
			</tr>

 	);
}

export default FlightListItem;