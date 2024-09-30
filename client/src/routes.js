import App from './App';

import HomePage from './components/HomePage';


import AboutPage from './components/AboutPage';
import UserPage from './components/UserPage';
import UserDetails from './components/UserDetails';
import HousePage from './components/HousePage';
// import HousesPage from from './components/AboutPage';
import CarPage from './components/CarPage';
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
            element: <HousePage />
        },


        // {
        //     path: "/houses/:id",
        //     element: <HouseDetails />
        // },

        {
            path: "/cars",
            element: <CarPage />
        }

        // {
        //     path: "/flights",
        //     element: <FlightsPage />
        // },
    
    ]
    }
];


export default routes;