import { useEffect, useState  } from 'react'
import { NavLink } from 'react-router-dom'
//import ProjectListItem from './ProjectListItem'

import CarList from './CarList'

function CarPage() {


  const [ cars, setCars ] = useState([])

  useEffect(() => {
    loadCars()
  }, []) 

  const loadCars = () => {
    fetch('http://127.0.0.1:5555/cars')
    .then(res => res.json())
    .then(data => setCars(data.cars))
  }

  
 
  return (
    // <section className="box">
    <section>
    {/* <h2>Hey!  Welcome to this CO2 Calculator.</h2>
    <p>
        Looking for an app to show the impact of today’s consumption from sources such as transportation, utilities, etc. 
        on CO2 produced and that based on the user’s input on  can provide an estimate of the amount of annual CO2 produced.
    </p> */}

    {/* <div style={{ margin: "60px 0" }}> */}
    <div style={{ margin: "0px 0" }}>

      {/* <HouseList houses={houses} /> */}
      <h1>Cars</h1>
      <CarList cars={cars} />
  
        {/* console.log(houses); */}
        {/* {
          houses.map(el => <HouseList house={el} key={el.id} />)
        } */}

    </div>

    

</section>
  )
}

export default CarPage