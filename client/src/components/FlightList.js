import { useState } from "react";
import FlightListItem from "./FlightListItem";

// function FlightList({ flights }) {

function FlightList({ flights, onDelete, onEdit }) {
	
	return (
		<section>

			<table className="table">
				<thead>
					<tr>
						<th>ID</th>
						<th>Number</th>
						<th>Departure</th>
						<th>Destination</th>
						<th>International ?</th>
						<th>Distance</th>
						<th>CO2 Produced</th>						
					</tr>
				</thead>
				<tbody>
					
				{flights.map((flight)=> (

					// <FlightListItem key={flight.id} flight={flight} />
					<FlightListItem key={flight.id} flight={flight} onDelete={onDelete} onEdit={onEdit} />
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

export default FlightList;