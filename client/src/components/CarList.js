import { useState } from "react";
import CarListItem from "./CarListItem";

function CarList({ cars }) {
	
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
						<th>Make</th>
						<th>Model</th>
						<th>Year</th>
						<th>mpg</th>
						<th>Miles Per Year</th>
						<th>Gasoline Consumed</th>
						<th>CO2 Produced</th>						
					</tr>
				</thead>
				<tbody>
					
				{cars.map((car)=> (

					<CarListItem key={car.id} car={car} />
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

export default CarList;