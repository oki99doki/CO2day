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

