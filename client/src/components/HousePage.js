import { useEffect, useState  } from 'react'
import { NavLink } from 'react-router-dom'
//import ProjectListItem from './ProjectListItem'

// import HouseList from './HouseList'
import HouseList2 from './HouseList2'

function HousePage() {


  const [ houses, setHouses ] = useState([])

  useEffect(() => {
    loadHouses()
  }, []) 

  const loadHouses = () => {
    //fetch('http://localhost:4000/users')
    fetch('http://127.0.0.1:5555/houses')
    .then(res => res.json())
    .then(data => setHouses(data.houses))
  }

  //const [houses, setHouses] = useState([])


  
 
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
      <h1>Houses</h1>
      <HouseList2 houses={houses} />
  
        {/* console.log(houses); */}
        {/* {
          houses.map(el => <HouseList house={el} key={el.id} />)
        } */}

    </div>

    

</section>
  )
}

export default HousePage