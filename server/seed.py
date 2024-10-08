#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import random

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Location, Car, House, Flight, Aircraft

import ipdb

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():

        print("Starting seed...")
        
        # Seed code goes here!

        # Clear existing data
        db.session.query(User).delete()
        db.session.query(Location).delete()
        db.session.query(Car).delete()
        db.session.query(House).delete()
        db.session.query(Flight).delete()
        db.session.query(Aircraft).delete()

        
        db.session.commit()


        # generate faker data


        
        users = []

    
        for _ in range(5):
            
            user = User(name = fake.name())

            users.append(user)
            db.session.add(user)
            
        db.session.commit()





        all_locations = [
            {'city': 'New York', 'state': 'NY', 'electricity_cost': 24.00, 'natural_gas_cost': 10.00, 'gasoline_cost': 3.60},
            {'city': 'Los Angeles', 'state': 'CA', 'electricity_cost': 22.50, 'natural_gas_cost': 9.50, 'gasoline_cost': 4.00},
            {'city': 'Chicago', 'state': 'IL', 'electricity_cost': 14.70, 'natural_gas_cost': 8.40, 'gasoline_cost': 3.20},
            {'city': 'Houston', 'state': 'TX', 'electricity_cost': 10.50, 'natural_gas_cost': 6.50, 'gasoline_cost': 3.00},
            {'city': 'Phoenix', 'state': 'AZ', 'electricity_cost': 12.30, 'natural_gas_cost': 7.00, 'gasoline_cost': 3.10},
            {'city': 'Philadelphia', 'state': 'PA', 'electricity_cost': 15.00, 'natural_gas_cost': 8.00, 'gasoline_cost': 3.50},
            {'city': 'San Antonio', 'state': 'TX', 'electricity_cost': 11.40, 'natural_gas_cost': 7.10, 'gasoline_cost': 3.05},
            {'city': 'San Diego', 'state': 'CA', 'electricity_cost': 23.00, 'natural_gas_cost': 9.20, 'gasoline_cost': 4.20},
            {'city': 'Dallas', 'state': 'TX', 'electricity_cost': 10.90, 'natural_gas_cost': 6.80, 'gasoline_cost': 3.15},
            {'city': 'San Jose', 'state': 'CA', 'electricity_cost': 25.50, 'natural_gas_cost': 10.00, 'gasoline_cost': 4.30},
            {'city': 'Austin', 'state': 'TX', 'electricity_cost': 11.90, 'natural_gas_cost': 7.50, 'gasoline_cost': 3.25},
            {'city': 'Jacksonville', 'state': 'FL', 'electricity_cost': 12.60, 'natural_gas_cost': 7.80, 'gasoline_cost': 3.30},
            {'city': 'San Francisco', 'state': 'CA', 'electricity_cost': 28.00, 'natural_gas_cost': 10.50, 'gasoline_cost': 4.50},
            {'city': 'Columbus', 'state': 'OH', 'electricity_cost': 13.40, 'natural_gas_cost': 8.20, 'gasoline_cost': 3.40},
            {'city': 'Indianapolis', 'state': 'IN', 'electricity_cost': 11.20, 'natural_gas_cost': 7.00, 'gasoline_cost': 3.00},
            {'city': 'Fort Worth', 'state': 'TX', 'electricity_cost': 10.70, 'natural_gas_cost': 6.70, 'gasoline_cost': 3.05},
            {'city': 'Charlotte', 'state': 'NC', 'electricity_cost': 12.80, 'natural_gas_cost': 8.00, 'gasoline_cost': 3.45},
            {'city': 'Seattle', 'state': 'WA', 'electricity_cost': 19.80, 'natural_gas_cost': 9.00, 'gasoline_cost': 4.10},
            {'city': 'Denver', 'state': 'CO', 'electricity_cost': 13.50, 'natural_gas_cost': 8.60, 'gasoline_cost': 3.75},
            {'city': 'Washington', 'state': 'DC', 'electricity_cost': 21.00, 'natural_gas_cost': 9.80, 'gasoline_cost': 3.90},
            {'city': 'Boston', 'state': 'MA', 'electricity_cost': 24.50, 'natural_gas_cost': 10.00, 'gasoline_cost': 4.20},
            {'city': 'El Paso', 'state': 'TX', 'electricity_cost': 11.00, 'natural_gas_cost': 6.60, 'gasoline_cost': 3.10},
            {'city': 'Nashville', 'state': 'TN', 'electricity_cost': 12.00, 'natural_gas_cost': 7.90, 'gasoline_cost': 3.35},
            {'city': 'Baltimore', 'state': 'MD', 'electricity_cost': 18.00, 'natural_gas_cost': 9.10, 'gasoline_cost': 3.70},
            {'city': 'Oklahoma City', 'state': 'OK', 'electricity_cost': 10.90, 'natural_gas_cost': 6.80, 'gasoline_cost': 3.00},
            {'city': 'Louisville', 'state': 'KY', 'electricity_cost': 12.50, 'natural_gas_cost': 7.40, 'gasoline_cost': 3.25},
            {'city': 'Portland', 'state': 'OR', 'electricity_cost': 19.50, 'natural_gas_cost': 9.50, 'gasoline_cost': 4.00},
            {'city': 'Milwaukee', 'state': 'WI', 'electricity_cost': 13.70, 'natural_gas_cost': 8.50, 'gasoline_cost': 3.60},
            {'city': 'Las Vegas', 'state': 'NV', 'electricity_cost': 13.00, 'natural_gas_cost': 7.50, 'gasoline_cost': 3.75},
            {'city': 'Albuquerque', 'state': 'NM', 'electricity_cost': 12.40, 'natural_gas_cost': 7.20, 'gasoline_cost': 3.20},
            {'city': 'Tucson', 'state': 'AZ', 'electricity_cost': 11.50, 'natural_gas_cost': 6.90, 'gasoline_cost': 3.15},
            {'city': 'Fresno', 'state': 'CA', 'electricity_cost': 21.30, 'natural_gas_cost': 9.60, 'gasoline_cost': 4.05},
            {'city': 'Sacramento', 'state': 'CA', 'electricity_cost': 22.40, 'natural_gas_cost': 9.70, 'gasoline_cost': 4.15},
            {'city': 'Long Beach', 'state': 'CA', 'electricity_cost': 23.70, 'natural_gas_cost': 9.80, 'gasoline_cost': 4.00},
            {'city': 'Kansas City', 'state': 'MO', 'electricity_cost': 11.00, 'natural_gas_cost': 6.40, 'gasoline_cost': 3.50},
            {'city': 'Mesa', 'state': 'AZ', 'electricity_cost': 11.20, 'natural_gas_cost': 6.60, 'gasoline_cost': 3.10},
            {'city': 'Virginia Beach', 'state': 'VA', 'electricity_cost': 12.90, 'natural_gas_cost': 7.30, 'gasoline_cost': 3.45},
            {'city': 'Atlanta', 'state': 'GA', 'electricity_cost': 13.40, 'natural_gas_cost': 7.80, 'gasoline_cost': 3.60},
            {'city': 'Colorado Springs', 'state': 'CO', 'electricity_cost': 12.50, 'natural_gas_cost': 7.50, 'gasoline_cost': 3.30},
            {'city': 'Omaha', 'state': 'NE', 'electricity_cost': 11.10, 'natural_gas_cost': 6.70, 'gasoline_cost': 3.20},
            {'city': 'Raleigh', 'state': 'NC', 'electricity_cost': 12.70, 'natural_gas_cost': 7.80, 'gasoline_cost': 3.55},
            {'city': 'Miami', 'state': 'FL', 'electricity_cost': 14.20, 'natural_gas_cost': 8.20, 'gasoline_cost': 3.70},
            {'city': 'Cleveland', 'state': 'OH', 'electricity_cost': 12.90, 'natural_gas_cost': 8.10, 'gasoline_cost': 3.40},
            {'city': 'Tulsa', 'state': 'OK', 'electricity_cost': 10.80, 'natural_gas_cost': 6.80, 'gasoline_cost': 3.00},
            {'city': 'Oakland', 'state': 'CA', 'electricity_cost': 23.20, 'natural_gas_cost': 9.40, 'gasoline_cost': 4.25},
            {'city': 'Minneapolis', 'state': 'MN', 'electricity_cost': 14.00, 'natural_gas_cost': 8.50, 'gasoline_cost': 3.80},
            {'city': 'Wichita', 'state': 'KS', 'electricity_cost': 10.50, 'natural_gas_cost': 6.40, 'gasoline_cost': 2.95},
            {'city': 'New Orleans', 'state': 'LA', 'electricity_cost': 12.50, 'natural_gas_cost': 7.90, 'gasoline_cost': 3.40},
            {'city': 'Arlington', 'state': 'TX', 'electricity_cost': 10.90, 'natural_gas_cost': 6.80, 'gasoline_cost': 3.10},
            {'city': 'Tampa', 'state': 'FL', 'electricity_cost': 12.90, 'natural_gas_cost': 8.10, 'gasoline_cost': 3.55},
            {'city': 'Bakersfield', 'state': 'CA', 'electricity_cost': 20.00, 'natural_gas_cost': 9.00, 'gasoline_cost': 4.00},
            {'city': 'Honolulu', 'state': 'HI', 'electricity_cost': 26.50, 'natural_gas_cost': 11.00, 'gasoline_cost': 4.50},
            {'city': 'Anaheim', 'state': 'CA', 'electricity_cost': 21.70, 'natural_gas_cost': 9.50, 'gasoline_cost': 4.00},
            {'city': 'Santa Ana', 'state': 'CA', 'electricity_cost': 22.00, 'natural_gas_cost': 9.80, 'gasoline_cost': 4.05},
            {'city': 'Corpus Christi', 'state': 'TX', 'electricity_cost': 11.70, 'natural_gas_cost': 6.70, 'gasoline_cost': 3.20},
            {'city': 'Riverside', 'state': 'CA', 'electricity_cost': 23.00, 'natural_gas_cost': 9.60, 'gasoline_cost': 4.25},
            {'city': 'Stockton', 'state': 'CA', 'electricity_cost': 21.50, 'natural_gas_cost': 9.40, 'gasoline_cost': 4.10},
            {'city': 'Chandler', 'state': 'AZ', 'electricity_cost': 12.20, 'natural_gas_cost': 7.00, 'gasoline_cost': 3.15},
            {'city': 'Chula Vista', 'state': 'CA', 'electricity_cost': 22.80, 'natural_gas_cost': 9.70, 'gasoline_cost': 4.20},
            {'city': 'Fort Wayne', 'state': 'IN', 'electricity_cost': 11.30, 'natural_gas_cost': 6.90, 'gasoline_cost': 3.00},
            {'city': 'Overland Park', 'state': 'KS', 'electricity_cost': 10.60, 'natural_gas_cost': 6.60, 'gasoline_cost': 2.90},
            {'city': 'Tempe', 'state': 'AZ', 'electricity_cost': 11.40, 'natural_gas_cost': 7.10, 'gasoline_cost': 3.10},
            {'city': 'Cape Coral', 'state': 'FL', 'electricity_cost': 12.80, 'natural_gas_cost': 7.90, 'gasoline_cost': 3.50},
            {'city': 'Frisco', 'state': 'TX', 'electricity_cost': 10.80, 'natural_gas_cost': 6.40, 'gasoline_cost': 3.00},
            {'city': 'Carrollton', 'state': 'TX', 'electricity_cost': 11.00, 'natural_gas_cost': 6.60, 'gasoline_cost': 3.05},
            {'city': 'Jersey City', 'state': 'NJ', 'electricity_cost': 16.50, 'natural_gas_cost': 8.50, 'gasoline_cost': 3.75},
            {'city': 'Bridgeport', 'state': 'CT', 'electricity_cost': 19.00, 'natural_gas_cost': 9.50, 'gasoline_cost': 3.90},
            {'city': 'Naperville', 'state': 'IL', 'electricity_cost': 13.80, 'natural_gas_cost': 8.00, 'gasoline_cost': 3.60},
            {'city': 'Chattanooga', 'state': 'TN', 'electricity_cost': 12.10, 'natural_gas_cost': 7.70, 'gasoline_cost': 3.30},
            {'city': 'Sunnyvale', 'state': 'CA', 'electricity_cost': 25.50, 'natural_gas_cost': 10.30, 'gasoline_cost': 4.40}
        ]

# Now the locations list contains 100 U.S. cities along with hypothetical cost data.


        #random_locations = random.sample(locations, 10)

        cities = []
        for _ in range(5):
            #ipdb.set_trace()
            city = random.choice(all_locations)
            location = Location(
                name = city['city'] + ", " + city['state'],
                gasolineCost = city['gasoline_cost'],
                electricityCost = city['electricity_cost'],
                gasCost = city['natural_gas_cost']
            )
            cities.append(location)
            #locations.append(location)
            db.session.add(location)
        db.session.commit()



        # # Print the selected locations
        # for location in random_locations:
        #     print(f"{location['city']}, {location['state']}: "
        #         f"Electricity: ${location['electricity_cost']/100:.2f}/kWh, "
        #         f"Natural Gas: ${location['natural_gas_cost']}/thousand ft³, "
        #         f"Gasoline: ${location['gasoline_cost']}/gallon")


        # Custom lists of makes and models
        # makes = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'Volkswagen']
        # models = ['Camry', 'Accord', 'F-150', 'Malibu', 'Altima', 'Jetta']

        # valid_combinations = {
        #    'Toyota': ['Camry', 'Corolla', 'RAV4'],
        #     'Honda': ['Accord', 'Civic', 'CR-V'],
        #     'Ford': ['F-150', 'Mustang', 'Explorer'],
        #     'Chevrolet': ['Malibu', 'Silverado', 'Equinox'],
        #     'Nissan': ['Altima', 'Sentra', 'Rogue'],
        #     'Volkswagen': ['Jetta', 'Golf', 'Tiguan']
        #     }
        
        valid_combinations = {
            'Toyota': {
                'Camry': {'mpg': 28},
                'Corolla': {'mpg': 32},
                'RAV4': {'mpg': 30}
            },
            'Honda': {
                'Accord': {'mpg': 30},
                'Civic': {'mpg': 33},
                'CR-V': {'mpg': 29}
            },
            'Ford': {
                'F-150': {'mpg': 24},
                'Mustang': {'mpg': 25},
                'Explorer': {'mpg': 22}
            },
            'Chevrolet': {
                'Malibu': {'mpg': 29},
                'Silverado': {'mpg': 21},
                'Equinox': {'mpg': 28}
            },
            'Nissan': {
                'Altima': {'mpg': 28},
                'Sentra': {'mpg': 30},
                'Rogue': {'mpg': 27}
            },
            'Volkswagen': {
                'Jetta': {'mpg': 30},
                'Golf': {'mpg': 31},
                'Tiguan': {'mpg': 24}
            }
        }


        
        # # Function to generate vehicle data
        # def generate_vehicle_data(num_vehicles):
        #     vehicle_data = []
            
        #     for _ in range(num_vehicles):
        #         # make = random.choice(list(valid_combinations.keys()))  # Randomly select a make
        #         # model = random.choice(valid_combinations[make])  # Select a valid model for that make
        #         make = random.choice(list(valid_combinations.keys()))
        #         model = random.choice(list(valid_combinations[make].keys()))
        #         mpg = valid_combinations[make][model]['mpg']

        #         vehicle = {
        #             'make': make,
        #             'model': model,
        #             'year': random.randint(1990, 2024),  # Random year between 1990 and 2023
        #             #'color': fake.color_name(),  # Random color
        #             'milesPerYear': random.randint(5000, 20000),  # Random miles per year
        #             'mpg': mpg
        #             }
        #         vehicle_data.append(vehicle)
            
        #     return vehicle_data

        # # Generate data for 10 vehicles
        # vehicles = generate_vehicle_data(10)


        cars = []


        no_users = 5
        values = list(range(1, no_users+1))
              
        random.shuffle(values)
        



        for _ in range(no_users):
            make = random.choice(list(valid_combinations.keys()))
            #model = random.choice(valid_combinations[make])
            model = random.choice(list(valid_combinations[make].keys()))
            # Select a random location from the dictionary list
            location = random.choice(all_locations)
            car = Car(
                #location_id = rc(locations).id,
                #location_id=location['id'],
                #location_id = None,
                user_id = values[_],
                location_id = fake.random_int(min=1, max=no_users),
                #location_id = random(locations)
                make = make,
                model = model,  #random.choice(valid_combinations[make]),
                year = fake.random_int(min=2002, max=2024),
                milesPerYear = fake.random_int(min=5000, max=20000),
                mpg = valid_combinations[make][model]['mpg'],
                co2Produced = fake.random_int(min=200, max=2000)
            )

            cars.append(car)
            db.session.add(car)
            
        db.session.commit()

        # # Add new individual customer cars e.g. like this (OPTIONAL)
        # newCar = Car(location_id=2, user_id=4, make = "Ferrari", model="F40", year=1996, milesPerYear=1500, mpg=14, co2Produced=300)
        # db.session.add(newCar)
        # db.session.commit()



        # Custom lists of makes and models
        styles = ['House', 'Townhouse', 'Condo', 'Apartment']
        sizes = ['small', 'medium', 'large', 'extra-large']

        houses = []

        #no_users = 5
        #values = list(range(1, no_users+1))
        # print(values)
      
        #random.shuffle(values)
        # print(values)
        # print(values)
    
        for _ in range(no_users):
            
            style = random.choice(styles)
            size = random.choice(sizes)
            
            house = House(
                #location_id = rc(locations).id,
                #location_id=location['id'],
                #location_id = None,
                #user_id = fake.random_int(min=1, max=5),
                user_id = values[_],
                location_id = fake.random_int(min=1, max=no_users),
                #location_id = random(locations)
                style = style,
                size = size,
                electricityDollars = fake.random_int(min=40, max=400),
                gasDollars = fake.random_int(min=30, max=300),
                electricityCo2Produced = fake.random_int(min=800, max=8000),
                gasCo2Produced = fake.random_int(min=600, max=6000)
            )

            houses.append(house)
            db.session.add(house)
            db.session.commit()



        flights_data = [
                {"number": "DL 87", "departure_city": "New York, NY", "destination_city": "London, UK", "is_international": True, "distance_miles": 3459},
                {"number": "AA 112", "departure_city": "Los Angeles, CA", "destination_city": "Chicago, IL", "is_international": False, "distance_miles": 1745},
                {"number": "UA 205", "departure_city": "San Francisco, CA", "destination_city": "Tokyo, Japan", "is_international": True, "distance_miles": 5145},
                {"number": "SW 365", "departure_city": "Houston, TX", "destination_city": "Miami, FL", "is_international": False, "distance_miles": 1090},
                {"number": "BA 279", "departure_city": "Boston, MA", "destination_city": "Dublin, Ireland", "is_international": True, "distance_miles": 3167},
                {"number": "WN 734", "departure_city": "Las Vegas, NV", "destination_city": "Phoenix, AZ", "is_international": False, "distance_miles": 298},
                {"number": "AF 18", "departure_city": "Newark, NJ", "destination_city": "Paris, France", "is_international": True, "distance_miles": 3885},
                {"number": "LH 441", "departure_city": "Seattle, WA", "destination_city": "Frankfurt, Germany", "is_international": True, "distance_miles": 4865},
                {"number": "DL 303", "departure_city": "Atlanta, GA", "destination_city": "Orlando, FL", "is_international": False, "distance_miles": 404},
                {"number": "VX 844", "departure_city": "San Diego, CA", "destination_city": "New York, NY", "is_international": False, "distance_miles": 2771},
                {"number": "NH 8", "departure_city": "Los Angeles, CA", "destination_city": "Tokyo, Japan", "is_international": True, "distance_miles": 5149},
                {"number": "SU 145", "departure_city": "New York, NY", "destination_city": "Moscow, Russia", "is_international": True, "distance_miles": 4666},
                {"number": "KL 204", "departure_city": "Atlanta, GA", "destination_city": "Amsterdam, Netherlands", "is_international": True, "distance_miles": 4759},
                {"number": "AA 145", "departure_city": "Miami, FL", "destination_city": "San Juan, Puerto Rico", "is_international": True, "distance_miles": 1020},
                {"number": "DL 517", "departure_city": "Washington, DC", "destination_city": "Boston, MA", "is_international": False, "distance_miles": 394},
                {"number": "QF 100", "departure_city": "Los Angeles, CA", "destination_city": "Sydney, Australia", "is_international": True, "distance_miles": 7498},
                {"number": "AC 882", "departure_city": "Toronto, Canada", "destination_city": "Vancouver, Canada", "is_international": False, "distance_miles": 1993},
                {"number": "CZ 900", "departure_city": "San Francisco, CA", "destination_city": "Beijing, China", "is_international": True, "distance_miles": 6926},
                {"number": "WN 342", "departure_city": "Dallas, TX", "destination_city": "Austin, TX", "is_international": False, "distance_miles": 194},
                {"number": "IB 6514", "departure_city": "Miami, FL", "destination_city": "Madrid, Spain", "is_international": True, "distance_miles": 4323}
            ]
        
        flights = []

        for _ in range(10):
            #ipdb.set_trace()
            flight_choice = random.choice(flights_data)
            flight = Flight(
                number = flight_choice['number'],
                departure = flight_choice['departure_city'],
                destination = flight_choice['destination_city'],
                international = flight_choice['is_international'],
                distance = flight_choice['distance_miles'],
                co2Produced = 1000,
                user_id = fake.random_int(min=1, max=5),
                aircraft_id = fake.random_int(min=1, max=10),
            )
            flights.append(flight)
            db.session.add(flight)
        db.session.commit()



        aircraft_data = [
            {
                "name": "Airbus A320",
                "max_range_miles": 3300,
                "avg_seats": 150,
                "fuel_consumption_gallons_per_100_passenger_miles": 3.2
            },
            {
                "name": "Boeing 737-800",
                "max_range_miles": 2935,
                "avg_seats": 160,
                "fuel_consumption_gallons_per_100_passenger_miles": 3.2
            },
            {
                "name": "Boeing 777-200ER",
                "max_range_miles": 6014,
                "avg_seats": 314,
                "fuel_consumption_gallons_per_100_passenger_miles": 3.5
            },
            {
                "name": "Airbus A330-300",
                "max_range_miles": 6350,
                "avg_seats": 277,
                "fuel_consumption_gallons_per_100_passenger_miles": 3.0
            },
            {
                "name": "Boeing 787-9 Dreamliner",
                "max_range_miles": 7530,
                "avg_seats": 296,
                "fuel_consumption_gallons_per_100_passenger_miles": 2.6
            },
            {
                "name": "Airbus A350-900",
                "max_range_miles": 8000,
                "avg_seats": 410,
                "fuel_consumption_gallons_per_100_passenger_miles": 2.9
            },
            {
                "name": "Boeing 747-8 Intercontinental",
                "max_range_miles": 7730,
                "avg_seats": 410,
                "fuel_consumption_gallons_per_100_passenger_miles": 3.6
            },
            {
                "name": "Embraer E195",
                "max_range_miles": 2300,
                "avg_seats": 120,
                "fuel_consumption_gallons_per_100_passenger_miles": 4.5
            },
            {
                "name": "Bombardier CRJ900",
                "max_range_miles": 2000,
                "avg_seats": 90,
                "fuel_consumption_gallons_per_100_passenger_miles": 5.0
            },
            {
                "name": "Airbus A220-300",
                "max_range_miles": 3400,
                "avg_seats": 160,
                "fuel_consumption_gallons_per_100_passenger_miles": 3.1
            }
        ]

        aircrafts = []

        for _ in range(10):
            #ipdb.set_trace()
            aircraft_choice = random.choice(aircraft_data)
            aircraft = Aircraft(
                name = aircraft_choice['name'],
                range = aircraft_choice['max_range_miles'],
                seats = aircraft_choice['avg_seats'],
                gallonsPer100Pass = aircraft_choice['fuel_consumption_gallons_per_100_passenger_miles']
            )
            aircrafts.append(aircraft)
            db.session.add(aircraft)
        db.session.commit()


        print("Seeding complete!")


        # generate intermediary result
        # commit intermediary results accordingly 