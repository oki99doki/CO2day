// import React, { useEffect, useState } from "react";
// import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
// import { Switch, Route } from "react-router-dom";

// function App() {
//   return (
//     <Router>
//       <NavBar user={user} setUser={setUser} />
//       <Routes>
//         <Route path="/" element={<HomePage />} />
//         <Route path="/users" element={<UserPage />} />
//         <Route path="/users/:id" element={<UserPage />} />
//         <Route path="/new-user-form" element={<NewUserForm />} />
        
//         <Route path="/houses" element={<HousesList />} />
//         <Route path="/cars" element={<CarsList />} />
//         <Route path="/flights" element={<FlightsList />} />
//         <Route path="/flights" element={<FlightsList />} />
        
        
        
        
//         {/*<Route path="/projects" element={<ProjectPage />} />
//         <Route path="/projects/:id" element={<ProjectPage/>} />
//         <Route path="/new-project-form" element={<NewProjectForm />} />
//         <Route path="/interests" element={<InterestList />} />
//         <Route path="/login" element={<Login />} />
//         <Route path="/signup" element={<SignUpForm />} /> */}
        
//       </Routes>
//     </Router>
//   );
// }



import { useState } from 'react'
import { Outlet } from 'react-router-dom'
import Header from "./components/Header";


function App() {

  const [darkMode, setDarkMode] = useState(true)

  const updateDarkMode = () => {
    setDarkMode(prevDarkMode => !prevDarkMode)
  }

  return (
    <div className={darkMode ? "App" : "App light"}>
      <Header updateDarkMode={updateDarkMode} darkMode={darkMode} />
      {/* ✅ 3b. Include the `Outlet` component in the `JSX`. */}
      <Outlet />
    </div>
  );
}


export default App;
