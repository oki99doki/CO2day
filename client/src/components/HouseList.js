import { useState } from "react";
import HouseListItem2 from "./HouseListItem2";

function HouseList({ houses }) {
	
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

			<ul>

				
				{houses.map((house)=> (

					<HouseListItem2 key={house.id} house={house} />
				))}
			</ul>

		</section>


		// <ul className="cards">
		//   {
		// 	houses.map(curHouse => {return <HouseListItem key={curHouse.id} house={curHouse} />})
		//   }
		// </ul>
	  );
	}

export default HouseList;