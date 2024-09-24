#from sqlalchemy.ext.associationproxy import association_proxy

# SK: added again 9/24
from config import db

# SK: comment out 9/24 - this is in config.py
#from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_serializer import SerializerMixin

# SK: comment out 9/24 - this is in config.py
#from sqlalchemy import MetaData





# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)

    # Info
    name = db.Column(db.String)

    # Relationship mapping user to related car
    car = db.relationship('Car', uselist=False, back_populates='user')

    # Relationship mapping user to related house
    house = db.relationship('House', uselist=False, back_populates='user')

    # Relationship mapping user to related flight
    flights = db.relationship('Flight', back_populates='user')


    def __repr__(self):
        return f'<User {self.id}, {self.name}>'
    


class Location(db.Model, SerializerMixin):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key = True)

    # Info
    name = db.Column(db.String)

    # Parameters
    electricityCost = db.Column(db.Float) # Parameter: Electricity Unit Cost in US$ per kWh
    gasCost = db.Column(db.Float) # Parameter: Natural Gas Unit Cost in US$ per Thousand cubic feet
    gasolineCost = db.Column(db.Float) # Parameter: Gasoline Unit Cost in US$ per Gallon

    # Relationship mapping the location to related cars
    cars = db.relationship('Car', back_populates="location")

    # Relationship mapping the location to related houses
    houses = db.relationship('House', back_populates="location")


    def __repr__(self):
        return f'<Location {self.id}, {self.name}, {self.electricityCost}, {self.gasCost}, {self.gasolineCost}>'


class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key = True)
    
    # Info
    make = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)

    # Input
    milesPerYear = db.Column(db.Float)
    mpg = db.Column(db.Float)

    # Intermdiary Calc. Results
    # co2perMile =  - This is calculated. Where should the calculation be located?

    # Output
    co2Produced = db.Column(db.Float) # Output: CO2 produced [kg CO2 / Year]

    # Foreign key to store the location id
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    
    # Foreign key to store the user id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationship mapping the car to related locations
    location = db.relationship('Location', back_populates="cars")

    # Relationship mapping car to related user
    user = db.relationship('User', back_populates='car')


    def __repr__(self):
        return f'<Car {self.id}, {self.make}, {self.model}, {self.year}, {self.milesPerYear}, {self.mpg}, {self.co2Produced}>'


class House(db.Model):
    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key = True)
    
    # Info
    style = db.Column(db.String)
    size = db.Column(db.String)
    
    # Input
    electricityDollars = db.Column(db.Float)
    gasDollars = db.Column(db.Float)

    # Intermdiary Calc. Results       
    # electricityConsumed - This is calculated. Where should the calculation be located?
    # gasConsumed - This is calculated.

    # Output
    electricityCo2Produced = db.Column(db.Float) # Output: CO2 produced due to electricity consumption [kg CO2 / Year]
    gasCo2Produced = db.Column(db.Float) # Output: CO2 produced due to natural gas consumption [kg CO2 / Year]
    
    # Foreign key to store the location id
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    
    # Foreign key to store the user id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationship mapping the house to related locations
    location = db.relationship('Location', back_populates="houses")

    # Relationship mapping house to related user
    user = db.relationship('User', back_populates='house')


    def __repr__(self):
        return f'<Car {self.id}, {self.style}, {self.size}, {self.electricityDollars}, {self.gasDollars}, {self.electricityCo2Produced}, {self.gasCo2Produced}>'


class Flight(db.Model):
    __tablename__ = 'flights'

    id = db.Column(db.Integer, primary_key = True)
    
    # Info
    number = db.Column(db.String)
    departure = db.Column(db.String)
    destination = db.Column(db.String)
    international = db.Column(db.Boolean)

    # Parameter
    distance = db.Column(db.Float) # Parameter: Distance between departure and destination airports in miles
    
    # Intermdiary Calc. Results
    # co2PerMile - This is calculated.
    # milesTraveled - This is calculated.

    # Output
    co2Produced = db.Column(db.Float) # Output: CO2 produced per trip (return flight)[kg CO2]

    # Foreign key to store the location id
    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircrafts.id'))
    
    # Foreign key to store the user id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationship mapping the flight to related aircrafts
    aircraft = db.relationship('Aircraft', back_populates="flights")

    # Relationship mapping flight to related user
    user = db.relationship('User', back_populates='flights')


    def __repr__(self):
        return f'<Flight {self.id}, {self.number}, {self.departure}, {self.destination}, {self.international}, {self.distance}, {self.co2Produced}>'


class Aircraft(db.Model):
    __tablename__ = 'aircrafts'

    id = db.Column(db.Integer, primary_key = True)

    # Info
    name = db.Column(db.String)
    range = db.Column(db.Integer)

    # Parameters
    seats = db.Column(db.Integer) # Parameter: Number of seats in aircraft
    gallonsPer100Pass = db.Column(db.Float) # Specific Fuel Consumption in Gallons per 100 passenger-miles

    # Relationship mapping aircraft to related flight
    flights = db.relationship('Flight', back_populates='aircraft')


    def __repr__(self):
        return f'<Aircraft {self.id}, {self.name}, {self.seats}, {self.gallonsPer100Pass}>'
