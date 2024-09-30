// import { FaPencilAlt, FaTrash } from "react-icons/fa";
import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";

// ✅ 5. Update `ProjectListItem`
// ✅ 6. Manage delete project.
function CarListItem({ car }) {
	//let { id, name, about, image, claps, link, phase } = user; // TO-DO: adapt this line with corresponding elements on left side
    //let { id, style } = house;
	const navigate = useNavigate();

	// const handleDelete = () => {
	// 	//fetch(`http://localhost:4000/houses/${house.id}`, {
	// 	fetch(`http://localhost:4000/houses/${house.id}`, {
	// 		method: "DELETE",
	// 	})
	// 		.then((res) => res.json())
	// 		.then(() => {
	// 			// ✅ 6a. On successful `DELETE` request redirect to `/projects`.
	// 			navigate("/houses");
	// 		});
	// };

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