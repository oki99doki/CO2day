
import { useState } from 'react'
import { Outlet } from 'react-router-dom'
import Header from "./components/Header";


function App() {

  const [darkMode, setDarkMode] = useState(false)

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
