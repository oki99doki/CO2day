# Phase 5 Full-Stack Application Capstone Project

# CO2day

## Description

"CO2day" is a "Carbon Footprint Calculator" app that contains a listing of data for miscellaneous factors with impact on CO2 produced and that based on the user’s input on today’s consumption (transportation, utilities, etc.) can provide an estimate of the amount of annual CO2 produced by the user.


## Wireframe

to be added.

Should include the following elements:

NavBar:
Home
User Profiles (with data)
Search (for inventory)
User profile - create new
Inventory (list of activities and their associated CO2 footprints for reference)
Examples by country - shows consumption (e.g. by country, etc.)
Energy Saving Tips

![WireframeHome](https://github.com/oki99doki/CO2day/blob/main/assets/WireframeHome.png)


## User Stories

1.	User can complete their profile including adding their CO2 categories (home energy, transportation, and Food & Waste) and entering consumption information and then get overview of CO2 footprint (lbs. CO2/ year)
2.	Navbar has Home (other user’s CO2 footprints), profiles (each user), list of activities (w. associated CO2 footprint for reference), energy saving tips, CO2 production by country (with per capita option.
3.	Home displays at least 10 user’s CO2 footprints (realistic fake numbers to show variety)
4.	User can click on each user profile and get detailed CO2 footprint information
5.	Other profiles display cards of all built-in user profiles (for reference)
6.	Users can click on other profiles page to view details regarding CO2 footprint
7.	Search box allows user to search within the other profiles menu
8.	User can look at inventory page to view list of activities and their associated CO2 footprints for reference)
9.	User can create own profile and fill in required information in input table based on categories (home energy, transportation, etc.)
10.	The app will provide instantaneous output about CO2 footprint based on user provided values


## Stretch Goals

1.	A KPI dashboard graphically shows the amount for each category (e.g. pie chart with relative size indicating the fractions and size+ numeric value providing total, or another chart or set of charts comparing to other users or avg. by country
2.	Add multiple charts and more advanced KPIs
3.	Allow user to persist data and enter multiple data sets so that relative changes over time can be shown numerically or displayed graphically indicating progress based on changes in user behavior


## React Tree Diagram

![ReactTree](https://github.com/oki99doki/CO2day/blob/main/assets/reactTree.png)


## Schema

![SchemaConcept](https://github.com/oki99doki/CO2day/blob/main/assets/concept.png)

![VariableNames](https://github.com/oki99doki/CO2day/blob/main/assets/variableNames.png)


## API Routes

**User Routes**

    GET /users: Retrieve a list of all users.

**Location Routes**
    
    GET /locations: Retrieve a list of all locations.

**Car Routes**
    
    GET /cars: Retrieve a list of all cars.

**House Routes**
    
    GET /houses: Retrieve a list of all houses.

**Flight Routes**
    
    GET /flights: Retrieve a list of all flights.
    
    POST /flights: Create a new flight.
    
    GET /flights/<id>: Retrieve a specific flight by ID.

    PATCH /flights/<id>: Update a specific flight by ID.
    
    DELETE /flights/<id>: Delete a specific flight by ID.

**Aircraft Routes**
    
    GET /aircrafts: Retrieve a list of all aircrafts.


## Kanban Board

https://trello.com/b/WCN6PLp7/phase-v-kanban

![TrelloBoard](https://github.com/oki99doki/CO2day/blob/main/assets/TrelloBoard.png)


## Constraints (optional)

- xxx


## Validations (optional)

- xxx


## Resources

- [EPA Carbon Footprint Tool](https://www3.epa.gov/carbon-footprint-calculator/)
- [Greenly Carbon Footprint Tool](https://www.carbonfootprint.com/calculator.aspx)
- [USA Today - Electricity rates by state (October 2024)](https://www.usatoday.com/money/homefront/deregulated-energy/electricity-rates-by-state/)
- [Choose Energy - Natural Gas Rates by State](https://www.chooseenergy.com/data-center/natural-gas-rates-by-state/)
- [AAA - Gas Prices by State](https://gasprices.aaa.com/)
