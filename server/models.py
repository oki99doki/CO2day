from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)


class Location(db.Model):
    __tablename__ = 'locations'

    pass


class House(db.Model):
    __tablename__ = 'houses'

    pass


class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key = True)
    
    make = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)

    milesPerYear = db.Column(db.Integer)
    mpg = db.Column(db.Integer)

    # co2perMile =  - This is calculated. Where should the calculation be located?

    co2Produced = db.Column(db.Float) # Output: CO2 produced [kg CO2 / Year]


class Flight(db.Model):
    __tablename__ = 'flights'

    pass


class Aircraft(db.Model):
    __tablename__ = 'aircrafts'

    pass


