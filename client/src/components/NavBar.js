// import React from "react";
// import { NavLink } from "react-router-dom";
// import './NavBar.css';

// function NavBar({ user, setUser }) {
//   function handleLogoutClick() {
//     fetch("/logout", { method: "DELETE" }).then((r) => {
//       if (r.ok) {
//         setUser(null);
//       }
//     });
//   }
//   return (
//     <header className="navbar">
//       <nav>
//         <ul className="nav-links">
//           <li className="nav-item"><NavLink to="/" className="nav-link" activeClassName="active">Home</NavLink></li>
//           <li className="nav-item"><NavLink to="/users" className="nav-link" activeClassName="active">Users</NavLink></li>
//           <li className="nav-item"><NavLink to="/projects" className="nav-link" activeClassName="active">Projects</NavLink></li>
//           <li className="nav-item"><NavLink to="/new-project-form" className="nav-link" activeClassName="active">New Project</NavLink></li>
//           <li className="nav-item"><NavLink to="/interests" className="nav-link" activeClassName="active">Interest List</NavLink></li>
//           {user ? (
//             <>
//               <li className="nav-item">
//                 <NavLink to="/" className="nav-link" onClick={handleLogoutClick}>
//                   Logout
//                 </NavLink>
//               </li>
//             </>
//           ) : (
//             <li className="nav-item">
//               <NavLink to="/login" className="nav-link" activeClassName="active">
//                 Login
//               </NavLink>
//             </li>
//           )}         
//         </ul>
//       </nav>
//     </header>
//   );
// }

// export default NavBar;