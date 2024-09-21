#from sqlalchemy_serializer import SerializerMixin
#from sqlalchemy.ext.associationproxy import association_proxy

#from config import db


from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_serializer import SerializerMixin

from sqlalchemy import MetaData


# contains definitions of tables and associated schema constructs
# read more about Metadata using the link at the bottom of the page
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)


# Models go here!

# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key = True)
#     userName = db.Column(db.String)


class Location(db.Model, SerializerMixin):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    #electricityCost = db.Column(db.Float) # Parameter: Electricity Unit Cost in US$ per kWh
    #gasCost = db.Column(db.Float) # Parameter: Natural Gas Unit Cost in US$ per Thousand cubic feet
    gasolineCost = db.Column(db.Float) # Parameter: Gasoline Unit Cost in US$ per Gallon

    # Relationship mapping the location to related cars
    cars = db.relationship('Car', back_populates="location")


# class House(db.Model):
#     __tablename__ = 'houses'

#     pass


class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key = True)
    
    make = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)

    milesPerYear = db.Column(db.Float)
    mpg = db.Column(db.Float)

    # co2perMile =  - This is calculated. Where should the calculation be located?

    co2Produced = db.Column(db.Float) # Output: CO2 produced [kg CO2 / Year]

    # Foreign key to store the location id
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    # Relationship mapping the car to related locations
    location = db.relationship('Location', back_populates="cars")


# class Flight(db.Model):
#     __tablename__ = 'flights'

#     pass


# class Aircraft(db.Model):
#     __tablename__ = 'aircrafts'

#     pass


