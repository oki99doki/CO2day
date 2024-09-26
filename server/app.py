#!/usr/bin/env python3

# STANDARD LIBRARY IMPORTS

from flask import Flask


# REMOTE LIBRARY IMPORTS

from flask import request, make_response

# SK: comment out 9/24 - this is in config.py
# from flask_migrate import Migrate


# LOCAL IMPORTS
from config import app, db #, api


# MODEL IMPORTS

# SK: comment out 9/24 - this is in config.py
# from models import db

from models import User, Location, Car, House, Flight, Aircraft


# OTHER IMPORTS
from collections import OrderedDict

import ipdb



# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


@app.route('/users')
def users():

    all_users = User.query.all()

    if all_users:

        user_dicts = []

        for user in all_users:

        #     total_co2_gasoline = 0

        #     for car in user.car:
        #         total_co2_gasoline += compute_co2_per_mile(user.car.mpg) * user.car.milesPerYear

            total_co2_flight = 0

            for flight in user.flights:

                #ipdb.set_trace()
                aircraftGallonsConsumed = compute_aircraftGallonsConsumed(flight.distance, flight.aircraft.gallonsPer100Pass, flight.aircraft.seats) # Gallons consumed for aircraft for flight

                aircraftCo2Produced = 10 * aircraftGallonsConsumed # CO2 produced for aircraft for flight

                co2Produced = aircraftCo2Produced / flight.aircraft.seats # CO2 produced for aircraft for flight

                total_co2_flight += co2Produced

            
            # Create a dictionary for each user
            user_dict = {
                'id': user.id,
                'name': user.name,

                'co2Produced_electricity': compute_electricityCo2Produced(compute_electricityConsumed(user.house.electricityDollars, user.house.location.electricityCost)),
                'co2Produced_gas': compute_gasCo2Produced(compute_gasConsumed(user.house.gasDollars, user.house.location.gasCost)),

                'co2Produced_gasoline': compute_co2_per_mile(user.car.mpg) * user.car.milesPerYear,
                # 'co2Produced_gasoline': total_co2_gasoline,

                'house_id': user.house.id,
                'location_id': user.house.location_id,
                
                'co2Produced_flight': total_co2_flight,

                'flight_id':  [flight.id for flight in user.flights],
                'aircraft_id': [flight.aircraft_id for flight in user.flights]


            }
            user_dicts.append(user_dict)

        body = {'users': user_dicts}  # List of all car dictionaries
        status = 200
    else:
        body = {'message': 'No users found.'}
        status = 404

    return make_response(body, status)



@app.route('/locations')
def locations():

    all_locations = Location.query.all()

    if all_locations:

        location_dicts = []

        for location in all_locations:
            
            # Create a dictionary for each user
            location_dict = {
                'id': location.id,
                'name': location.name,
                'electricityCost': location.electricityCost,
                'gasCost': location.gasCost,
                'gasolineCost': location.gasolineCost,
            }
            location_dicts.append(location_dict)

        body = {'locations': location_dicts}  # List of all car dictionaries
        status = 200
    else:
        body = {'message': 'No locations found.'}
        status = 404

    return make_response(body, status)



@app.route('/cars')
def cars():

    all_cars = Car.query.all()

    if all_cars:

        car_dicts = []

        for car in all_cars:

            # Compute gallons consumed by car per year
            gasolineConsumed = car.milesPerYear / car.mpg
            
            # Compute CO2 produced per mile
            co2_per_mile = compute_co2_per_mile(car.mpg)

            # You can also compute total CO2 for the year if needed
            total_co2 = co2_per_mile * car.milesPerYear

            # Create a dictionary for each car
            car_dict = {
                'id': car.id,
                'make': car.make,
                'model': car.model,
                'year': car.year,
                'milesPerYear': car.milesPerYear,
                'mpg': car.mpg,
                'gasolineConsumed': gasolineConsumed,
                'co2PerMile': co2_per_mile,
                'co2Produced': total_co2  # You can choose to save co2_per_mile if needed
            }
            car_dicts.append(car_dict)

        body = {'cars': car_dicts}  # List of all car dictionaries
        status = 200
    else:
        body = {'message': 'No cars found.'}
        status = 404

    return make_response(body, status)

# Helper Function
def compute_co2_per_mile(mpg):
    CO2_per_gallon = 8.89  # kg CO2 produced per gallon
    co2_per_mile = CO2_per_gallon / mpg
    return co2_per_mile
    


@app.route('/houses')
def houses():

    all_houses = House.query.all()

    if all_houses:

        house_dicts = []

        for house in all_houses:
            
            # Compute electricity consumed per year in kWh
            electricityConsumed = compute_electricityConsumed(house.electricityDollars, house.location.electricityCost)

            # CO2 produced per year due to electricity consumption in kg CO2
            electricityCo2Produced = compute_electricityCo2Produced(electricityConsumed)

            # Compute gas consumed per year in 1000 cubic feet
            gasConsumed = compute_gasConsumed(house.gasDollars, house.location.gasCost)

            # CO2 produced per year due to gas consumption in kg CO2
            gasCo2Produced = compute_gasCo2Produced(gasConsumed)
           
            # Create a dictionary for each house
            house_dict = {
                'id': house.id,
                'style': house.style,
                'size': house.size,

                'electricityDollars': house.electricityDollars,
                'electricityConsumed': electricityConsumed,
                'electricityCost':  house.location.electricityCost,
                'electricityCo2Produced': electricityCo2Produced, #electricity_co2

                'gasDollars': house.gasDollars,
                'gasConsumed': gasConsumed,
                'gasCost':  house.location.gasCost,
                'gasCo2Produced': gasCo2Produced, #gas_co2

                'Co2Produced': electricityCo2Produced + gasCo2Produced, #electricity_and_gas_combined_co2

                'user_id': house.user_id,
                'location_id': house.location_id
            }
            house_dicts.append(house_dict)

        body = {'houses': house_dicts}  # List of all car dictionaries
        status = 200
    else:
        body = {'message': 'No houses found.'}
        status = 404

    return make_response(body, status)


# Helper Functions
def compute_electricityConsumed(electricityDollars, electricityCost):
    electricityConsumed = electricityDollars * 12 / (electricityCost/100)
    return electricityConsumed

def compute_electricityCo2Produced(electricityConsumed):
    electricityCo2Produced = electricityConsumed * 0.369
    return electricityCo2Produced

def compute_gasConsumed(gasDollars, gasCost):
    gasConsumed = gasDollars * 12 / (gasCost)
    return gasConsumed

def compute_gasCo2Produced(gasConsumed):
    gasCo2Produced = gasConsumed * 54.44
    return gasCo2Produced


#((house.electricity_dollars * 12) / location.electricty_cost ) * 0.369 = cotwo_per_house
# @app.route('/extra_special_calc/<int:user_id>')
# def calculate_yearly_house_co2():
#     # query for all data necessary

#     # calculate final numbers

#     # send back final numbers
#     return make_response({
#         "final_calc": amount,
#         "house_id": house.id,
#         "location": location.to_dict(),
#         "anything_else": "no"
#     }, 200)


# @app.route('/house', methods=["POST"])
# def create_house():
#     data = request.get_json()

    #create intermediary results

    #commit all info including intermediary results to db 



@app.route('/flights')
def flights():

    all_flights = Flight.query.all()

    if all_flights:

        flight_dicts = []

        for flight in all_flights:
            
            
            aircraftGallonsConsumed = compute_aircraftGallonsConsumed(flight.distance, flight.aircraft.gallonsPer100Pass, flight.aircraft.seats) # Gallons consumed for aircraft for flight

            aircraftCo2Produced = 10 * aircraftGallonsConsumed # CO2 produced for aircraft for flight

            co2Produced = aircraftCo2Produced / flight.aircraft.seats # CO2 produced for aircraft for flight
        
            # CO2 produced per flight and passenger in kg CO2
            aircraftCo2Produced

            # Create a dictionary for each flight
            flight_dict = {
                'id': flight.id,
                'name': flight.number,
                'departure': flight.departure,
                'destination': flight.destination,
                'international': flight.international,

                'distance': flight.distance,
                #'co2Produced': flight.co2Produced, - commented out: this is old constant value still in seed.py of 1000
                'co2Produced': co2Produced,

                'user_id': flight.user_id,
                'aircraft_id': flight.aircraft_id
            }
            flight_dicts.append(flight_dict)

        body = {'flights': flight_dicts}  # List of all flight dictionaries
        status = 200
    else:
        body = {'message': 'No flights found.'}
        status = 404

    return make_response(body, status)

# Helper Functions
def compute_aircraftGallonsConsumed(distance, gallonsPer100Pass, seats):
    aircraftGallonsConsumed = (2 * distance) * gallonsPer100Pass * (seats/100)
    return aircraftGallonsConsumed



@app.route('/aircrafts')
def aircrafts():

    all_aircrafts = Aircraft.query.all()

    if all_aircrafts:

        aircraft_dicts = []

        for aircraft in all_aircrafts:
            
            # Create a dictionary for each flight
            aircraft_dict = {
                'id': aircraft.id,
                'name': aircraft.name,
                'range': aircraft.range,
                'seats': aircraft.seats,
                'gallonsPer100Pass': aircraft.gallonsPer100Pass                
            }
            aircraft_dicts.append(aircraft_dict)

        body = {'aircrafts': aircraft_dicts}  # List of all flight dictionaries
        status = 200
    else:
        body = {'message': 'No faircrafts found.'}
        status = 404

    return make_response(body, status)



if __name__ == '__main__':
    app.run(port=5555, debug=True)

