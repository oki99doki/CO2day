import { useEffect, useState  } from 'react'
import { NavLink } from 'react-router-dom'
//import ProjectListItem from './ProjectListItem'

function Home() {

  const [topFive, setTopFive] = useState([])

  //✅ 9. Create homepage with top 5 liked projects.
  useEffect(() => {
    fetch('http://localhost:4000/projects?_sort=claps&_order=desc&_limit=5')
    .then(res => res.json())
    .then(data => setTopFive(data))
  }, [])

  return (
    <section className="box">
    <h2>Hey!  View Awesome Projects.</h2>
    <p>
        Looking for someone to hire? Check out these awesome projects from
        Flatiron students.
    </p>

    <div style={{ margin: "60px 0" }}>
        <NavLink to={"/projects"}>
          <button className="button" >
              View All Projects
          </button>
        </NavLink>
        {
          topFive.map(el => <ProjectListItem project={el} key={el.id} />)
        }

    </div>

    

</section>
  )
}

export default Home