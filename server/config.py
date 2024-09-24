# STANDARD LIBRARY IMPORTS

from flask import Flask


# REMOTE LIBRARY IMPORTS

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# from flask_cors import CORS

# from flask_restful import Api


# LOCAL IMPORTS





## Instantiate app, set attributes

# create a Flask application object
app = Flask(__name__)

# configure a database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ...
app.json.compact = False


# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
 })

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)



## Instantiate REST API
# api = Api(app)

## Instantiate CORS
# CORS(app)