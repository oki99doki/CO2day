import { useState } from "react";
import HouseListItem2 from "./HouseListItem2";

function HouseList2({ houses }) {
	
	//const [searchQuery, setSearchQuery] = useState("");
	//const [phaseState, setPhase] = useState(0);
	//const [searchQuery, setSearchQuery] = useState("");
	//const [houses, setHouses] = useState([])

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

			<table className="table">
				<thead>
					<tr>
						<th>ID</th>
						<th>Style</th>
						<th>Size</th>
						<th>Electricity Cost</th>
						<th>Gas Cost</th>
						<th>Electricity CO2</th>
						<th>Gas CO2</th>
					</tr>
				</thead>
				<tbody>
					
				{houses.map((house)=> (

					<HouseListItem2 key={house.id} house={house} />
				))}
		
				</tbody>
			</table>
			

		</section>


		// <ul className="cards">
		//   {
		// 	houses.map(curHouse => {return <HouseListItem key={curHouse.id} house={curHouse} />})
		//   }
		// </ul>
	  );
	}

export default HouseList2;