// import { FaPencilAlt, FaTrash } from "react-icons/fa";
import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";

// ✅ 5. Update `ProjectListItem`
// ✅ 6. Manage delete project.
function UserListItem({ user }) {
	//let { id, name, about, image, claps, link, phase } = user; // TO-DO: adapt this line with corresponding elements on left side
    let { id, name } = user;
	const navigate = useNavigate();

	// const handleDelete = () => {
	// 	fetch(`http://localhost:4000/projects/${user.id}`, {
	// 		method: "DELETE",
	// 	})
	// 		.then((res) => res.json())
	// 		.then(() => {
	// 			// ✅ 6a. On successful `DELETE` request redirect to `/projects`.
	// 			navigate("/users");
	// 		});
	//};

	return (




		<tr key={user.id}>
				<td>{user.id}</td>
				<td>{user.name}</td>
				{/* <td>{house.size}</td>
				<td>${house.electricityDollars}</td>
				<td>${house.gasDollars}</td>
				<td>{house.electricityCo2Produced.toFixed(1)} kg</td>
				<td>{house.gasCo2Produced.toFixed(1)} kg</td> */}
			</tr>

		



	);
}

export default UserListItem;