import { useEffect, useState  } from 'react'
import { NavLink } from 'react-router-dom'
//import ProjectListItem from './ProjectListItem'

// import HouseList from './HouseList'
import HouseList2 from './HouseList2'

function HousePage() {


  // const [ houses, setHouses ] = useState([])

  // useEffect(() => {
  //   loadHouses()
  // }, []) 

  // const loadHouses = () => {
  //   //fetch('http://localhost:4000/users')
  //   fetch('http://127.0.0.1:5555/houses')
  //   .then(res => res.json())
  //   .then(data => setHouses(data))
  // }

  //const [houses, setHouses] = useState([])


  const houses =  [
        {
            "Co2Produced": 21541.307142857142,
            "electricityCo2Produced": 11742.107142857145,
            "electricityConsumed": 31821.428571428576,
            "electricityCost": 11.2,
            "electricityDollars": 297.0,
            "gasCo2Produced": 9799.199999999999,
            "gasConsumed": 180.0,
            "gasCost": 6.6,
            "gasDollars": 99.0,
            "id": 1,
            "location_id": 1,
            "size": "extra-large",
            "style": "Apartment",
            "user_id": 5
        },
        {
            "Co2Produced": 26833.99462527286,
            "electricityCo2Produced": 6754.230414746544,
            "electricityConsumed": 18304.14746543779,
            "electricityCost": 21.7,
            "electricityDollars": 331.0,
            "gasCo2Produced": 20079.764210526315,
            "gasConsumed": 368.8421052631579,
            "gasCost": 9.5,
            "gasDollars": 292.0,
            "id": 2,
            "location_id": 4,
            "size": "medium",
            "style": "Apartment",
            "user_id": 2
        },
        {
            "Co2Produced": 15624.44705311666,
            "electricityCo2Produced": 1183.520737327189,
            "electricityConsumed": 3207.373271889401,
            "electricityCost": 21.7,
            "electricityDollars": 58.0,
            "gasCo2Produced": 14440.926315789471,
            "gasConsumed": 265.2631578947368,
            "gasCost": 9.5,
            "gasDollars": 210.0,
            "id": 3,
            "location_id": 4,
            "size": "extra-large",
            "style": "Condo",
            "user_id": 1
        },
        {
            "Co2Produced": 11652.706666666665,
            "electricityCo2Produced": 7660.44,
            "electricityConsumed": 20760.0,
            "electricityCost": 20.0,
            "electricityDollars": 346.0,
            "gasCo2Produced": 3992.2666666666664,
            "gasConsumed": 73.33333333333333,
            "gasCost": 9.0,
            "gasDollars": 55.0,
            "id": 4,
            "location_id": 2,
            "size": "large",
            "style": "House",
            "user_id": 3
        },
        {
            "Co2Produced": 13736.78,
            "electricityCo2Produced": 2413.2599999999998,
            "electricityConsumed": 6540.0,
            "electricityCost": 20.0,
            "electricityDollars": 109.0,
            "gasCo2Produced": 11323.52,
            "gasConsumed": 208.0,
            "gasCost": 9.0,
            "gasDollars": 156.0,
            "id": 5,
            "location_id": 2,
            "size": "large",
            "style": "Condo",
            "user_id": 4
        }
    ]

  
 
  return (
    // <section className="box">
    <section>
    {/* <h2>Hey!  Welcome to this CO2 Calculator.</h2>
    <p>
        Looking for an app to show the impact of today’s consumption from sources such as transportation, utilities, etc. 
        on CO2 produced and that based on the user’s input on  can provide an estimate of the amount of annual CO2 produced.
    </p> */}

    <div style={{ margin: "60px 0" }}>

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