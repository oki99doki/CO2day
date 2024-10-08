// import { FaPencilAlt, FaTrash } from "react-icons/fa";
import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";

// ✅ 5. Update `ProjectListItem`
// ✅ 6. Manage delete project.
function CarListItem({ car }) {
	//let { id, name, about, image, claps, link, phase } = user; // TO-DO: adapt this line with corresponding elements on left side
    //let { id, style } = house;
	const navigate = useNavigate();


	return (
		        
			<tr key={car.id}>
				<td>{car.id}</td>
				<td>{car.make}</td>
				<td>{car.model}</td>
				<td>{car.year}</td>
				<td>{car.mpg}</td>
				<td>{car.milesPerYear}</td>
				<td>{car.gasolineConsumed.toFixed(1)}</td>
				<td>{car.co2Produced.toFixed(1)} kg</td>
			</tr>

 	);
}

export default CarListItem;