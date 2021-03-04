# Import dependencies
import numpy as nu
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
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
        f"api/v1.0/(yyyy-mm-dd)<br/>"
        f"api/v1.0/(yyyy-mm-dd)/(yyyy-mm-dd)"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).all()

    session.close()
    
    # Create a dictionary from the row data and append to a list of results
    precip_list = []
    for item in results:
        precip_dict = {}
        precip_dict["date"] = item[0]
        precip_dict["prcp"] = item[1]
        precip_list.append(precip_dict)

    return jsonify(precip_list)

   
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(Station.station, Station.name).all()

    session.close()

    # Create a dictionary from the row data and append to a list of results
    station_list = []
    for item in results:
        station_dict = {}
        station_dict["station"] = item[0]
        station_dict["name"] = item[1]
        station_list.append(station_dict)

    return jsonify(station_list)
   

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.tobs)\
        .filter(Station.station == 'USC00519281')\
        .filter(Measurement.date >= '2016-08-24')\
        .order_by(Measurement.date).all()

    session.close()
    
    # Create a dictionary from the row data and append to a list of results
    tobs_list = []
    for item in results:
        tobs_dict = {}
        tobs_dict["date"] = item[0]
        tobs_dict["tobs"] = item[1]
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>/<end>")
def start_to_end_date(start_to_end):
# Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
        .filter(Measurement.date >= start_to_end).all()
    
    session.close()

# /api/v1.0/<start> and /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.



if __name__ == "__main__":
    app.run(debug=True)