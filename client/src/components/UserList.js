import { useState } from "react";
import UserListItem from "./UserListItem";

function UserList({ users }) {
	//const [searchQuery, setSearchQuery] = useState("");
	//const [phaseState, setPhase] = useState(0);
	//const [searchQuery, setSearchQuery] = useState("");
	//const [users, setUsers] = useState([])

	// const filteredUsers = users.filter(
	// 	(user) => {
	// 		// return (
	// 		// 	(phaseState === 0 || user.phase === phaseState) &&
	// 		// 	(searchQuery === '' || user.name.toLowerCase().includes(searchQuery.toLowerCase()))
	// 		// )
	// 		return (
	// 			searchQuery === '' || user.name.toLowerCase().includes(searchQuery.toLowerCase())
	// 		)
	// 	}
	// );

	return (
		<section>
			<h2>User List</h2>
			<div className="filter">
				{/* <button onClick={() => setPhase(0)}>All</button> */}
				{/* <button onClick={() => setPhase(5)}>Phase 5</button>
				<button onClick={() => setPhase(4)}>Phase 4</button>
				<button onClick={() => setPhase(3)}>Phase 3</button>
				<button onClick={() => setPhase(2)}>Phase 2</button>
				<button onClick={() => setPhase(1)}>Phase 1</button> */}
				<p>blabla    </p>
			</div>
			{/* <input
				type="text"
				placeholder="Search..."
				name="search"
				value={searchQuery}
				onChange={(e) => setSearchQuery(e.target.value)}
			/> */}
			<ul className="cards">
				{/* {filteredUsers.map((user) => ( */}
				{users.map((user) => (
					
					
					<UserListItem key={user.id} user={user} />
					// <p> Test blabla ... </p>
				))}
			</ul>
		</section>
	);
}

export default UserList;