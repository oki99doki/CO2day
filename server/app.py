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
            
            # Create a dictionary for each user
            user_dict = {
                'id': user.id,
                'name': user.name
            }
            user_dicts.append(user_dict)

        body = {'users': user_dicts}  # List of all car dictionaries
        status = 200
    else:
        body = {'message': 'No users found.'}
        status = 404

    return make_response(body, status)




@app.route('/cars')
def cars():

    all_cars = Car.query.all()

    if all_cars:
        car_dicts = []
        for car in all_cars:
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

    location = Location.query.all()

    if all_houses:
        house_dicts = []
        for house in all_houses:

            # Compute CO2 produced per mile
            #((house.electricity_dollars * 12) / location.electricty_cost ) * 0.369 = cotwo_per_house
            #electricity_co2 = compute_electricityConsumed(house.electricityDollars) * 0.369

            #gas_co2 = compute_co2_per_mile(car.mpg)
            # You can also compute total CO2 for the year if needed
            #total_co2 = co2_per_mile * car.milesPerYear
            #total_co2 = 
           
            # Create a dictionary for each house
            house_dict = {
                'id': house.id,
                'style': house.style,
                'size': house.size,
                'electricityDollars': house.electricityDollars,
                #'gasDollars': house.gasDollars,
                'electricityCo2Produced': compute_electricityConsumed(house.electricityDollars, location.electricityCost) * 0.369 #electricity_co2
                #'gasCo2Produced': house.gasCo2Produced
                #'co2Produced': total_co2  # You can choose to save co2_per_mile if needed
            }
            house_dicts.append(house_dict)

        body = {'houses': house_dicts}  # List of all car dictionaries
        status = 200
    else:
        body = {'message': 'No houses found.'}
        status = 404

    return make_response(body, status)


# Helper Function
def compute_electricityConsumed(electricityDollars, location):
    electricityConsumed = electricityDollars * 12 / location.electricityCost
    return electricityConsumed



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


if __name__ == '__main__':
    app.run(port=5555, debug=True)

