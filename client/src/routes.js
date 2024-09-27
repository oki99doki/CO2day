import App from "./App";

import HomePage from './components/HomePage';


// import AboutPage
// import UserPage
// import UserDetails
// import HousesPage
// import CarsPage
// import FlightsPage




const routes = [

    {
        path: "/",
        element: <App />,

        children: [{

            path: "/",
            element: <HomePage />
        },

        {
            path: "/about",
            element: <AboutPage />
        },

        {
            path: "/users",
            element: <UserPage />
        },

        {
            path: "/users/:id",
            element: <UserDetails />
        },

        {
            path: "/houses",
            element: <HousesPage />
        },

        {
            path: "/cars",
            element: <CarsPage />
        },

        {
            path: "/flights",
            element: <FlightsPage />
        },
    
    ]
    }
];


export default routes;