#!/usr/bin/env python3

# Standard library imports

# # Remote library imports
# from flask import request
# from flask_restful import Resource

# # Local imports
# from config import app, db, api
# # Add your model imports



from flask import Flask

from flask import request, make_response

from flask_migrate import Migrate

from models import db

from models import Location, Car

import ipdb

# create a Flask application object
app = Flask(__name__)

# configure a database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


@app.route('/cars')
def cars():

    #ipdb.set_trace()
    # car = Car.query.first()

    # #car_dict = [car.to_dict() for car in cars]

    # if car:
    #     body = {'id': car.id,
    #         'maken': car.make,
    #         'model': car.model,
    #         'year': car.year,
    #         'milesPerYear': car.milesPerYear,
    #         'mpg': car.mpg,
    #         'co2Produced': car.co2Produced
    #         }
    #     status = 200
    # else:
    #     body = {'message': f'Car {id} not found.'}
    #     status = 404
    #return make_response(body, status)

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

