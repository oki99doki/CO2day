// import { FaPencilAlt, FaTrash } from "react-icons/fa";
import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";

// ✅ 5. Update `ProjectListItem`
// ✅ 6. Manage delete project.
function UserListItem({ user }) {
	//let { id, name, about, image, claps, link, phase } = user; // TO-DO: adapt this line with corresponding elements on left side
    let { id, name } = user;
	const navigate = useNavigate();

	const handleDelete = () => {
		fetch(`http://localhost:4000/projects/${user.id}`, {
			method: "DELETE",
		})
			.then((res) => res.json())
			.then(() => {
				// ✅ 6a. On successful `DELETE` request redirect to `/projects`.
				navigate("/users");
			});
	};

	return (
		<li className="card">
			{/* <figure className="image">
				<img src={image} alt={name} />
			</figure> */}
			<section className="details">
			{/* ✅ 5a. Create a `NavLink` for each project that redirects to `ProjectDetails`.  */}
			{/* ✅ - The link is to `/projects/:id` */}
			{/* ✅ 5b. Use a fetch request in `ProjectDetails` to access a single project.  Use `useParams` to access the id. */}
				<NavLink to={`/users/${id}`}>
					<h4>{name}</h4>
				</NavLink>
				{/* <p>{about}</p>
				<p>
					<a href={link}>Link</a>
				</p> */}
			</section>

			{/* <footer className="extra">
				<span className="badge blue">Phase {phase}</span>
				<div className="manage">
					<button class="manage-button">
						<NavLink to={`/users/${id}/edit`}>
							<FaPencilAlt />
						</NavLink>
					</button>
					<button onClick={() => handleDelete()}>
						<FaTrash />
					</button>
				</div>
			</footer> */}
		</li>
	);
}

export default UserListItem;