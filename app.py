# Import packages
import numpy as nu

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Sessions
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask setup
app = Flask(__name__)

# Setup Falsk Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"api/v1.0/precipitation<br/>"
        f"api/v1.0/stations<br/>"
        f"api/v1.0/tobs<br/>"
        f"api/v1.0/<start><br/>"
        f"api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)


   

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)


    

@app.route("/api/v1.0/<start>")
def start_date():
    # Create our session (link) from Python to the DB
    session = Session(engine)


    

@app.route("/api/v1.0/<start>/<end>")
def start_to_end_date():
# Create our session (link) from Python to the DB
    session = Session(engine)


    



if __name__ == "__main__":
    app.run(debug=True)
