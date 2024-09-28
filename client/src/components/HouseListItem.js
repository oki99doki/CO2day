// import { FaPencilAlt, FaTrash } from "react-icons/fa";
import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";

// ✅ 5. Update `ProjectListItem`
// ✅ 6. Manage delete project.
function HouseListItem({ house }) {
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
		<li className="card">
			
			<h2>{house.style}</h2>
			{/* <p>Size: {house.size}</p>
            <p>Electricity Cost: ${house.electricityDollars} (CO2: {house.electricityCo2Produced} kg)</p>
            <p>Gas Cost: ${house.gasDollars} (CO2: {house.gasCo2Produced} kg)</p> */}


			<table>
                <thead>
                    <tr>
                        <th>Parameter</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>ID</td>
                        <td>{house.id}</td>
                    </tr>
                    <tr>
                        <td>Style</td>
                        <td>{house.style}</td>
                    </tr>
                    <tr>
                        <td>Size</td>
                        <td>{house.size}</td>
                    </tr>
                    <tr>
                        <td>Electricity Cost</td>
                        <td>${house.electricityDollars} (CO2: {house.electricityCo2Produced.toFixed(1)} kg)</td>
                    </tr>
                    <tr>
                        <td>Gas Cost</td>
                        <td>${house.gasDollars} (CO2: {house.gasCo2Produced.toFixed(1)} kg)</td>
                    </tr>
                </tbody>
            </table>

			

			{/* <footer className="extra">
				<span className="badge blue">Phase {phase}</span>
				<div className="manage">
					<button class="manage-button">
						<NavLink to={`/users/${id}/edit`}>
							<FaPencilAlt />
						</NavLink>
					</button>
					<button onClick={() => handleDelete()}>
						<FaTrash />
					</button>
				</div>
			</footer> */}
		</li>
	);
}

export default HouseListItem;