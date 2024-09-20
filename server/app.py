#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

#((house.electricity_dollars * 12) / location.electricty_cost ) * 0.369 = cotwo_per_house
@app.route('/extra_special_calc/<int:user_id>')
def calculate_yearly_house_co2():
    # query for all data necessary

    # calculate final numbers

    # send back final numbers
    return make_response({
        "final_calc": amount,
        "house_id": house.id,
        "location": location.to_dict(),
        "anything_else": "no"
    }, 200)


@app.route('/house', methods=["POST"])
def create_house():
    data = request.get_json()

    #create intermediary results

    #commit all info including intermediary results to db 


if __name__ == '__main__':
    app.run(port=5555, debug=True)

