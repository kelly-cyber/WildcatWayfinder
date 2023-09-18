import json

from flask import Flask, render_template, redirect, request, url_for
import requests
from bson import json_util
from flask_googlemaps import GoogleMaps, Map

app = Flask(__name__)


# key: AIzaSyBV6xo3duC37B7z4RGcamphREa2ZyDhtbQ

@app.route('/map')
def show_map():
    start = request.args.get('start')
    end = request.args.get('end')
    waypoints = request.args.get('waypoints')
    travel_mode = request.args.get('travel_mode')
    return render_template('map.html', start=start, end=end, waypoints=waypoints, travel_mode=travel_mode)  # Add travel_mode parameter here



@app.route('/submit-path', methods=['POST'])
def submit_path():
    start = request.form['start']
    end = request.form['end']
    waypoints = request.form.getlist('waypoints')
    travel_mode = request.form['travel_mode']

    # Join waypoints with ";" separator to pass them as a single string to the map.html template
    waypoints_str = ';'.join(waypoints)

    return redirect(url_for('show_map', start=start, end=end, waypoints=waypoints_str, travel_mode=travel_mode))  # Add travel_mode parameter here



@app.route('/geocode')
def geocode():
    address = request.args.get('address')
    api_key = 'AIzaSyBV6xo3duC37B7z4RGcamphREa2ZyDhtbQ'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    return json.dumps(data)


@app.route('/')
def index():
    return render_template('index.html')


# Define a route to display the records
@app.route('/records')
def records():
    # push list of dictionaries to the template
    # Load the response of ReadRecords() into a list of dictionaries
    response = requests.get('https://unhcampusdirections.azurewebsites.net/api/readrecords').text  # change to your API endpoint
    list_of_dicts = json_util.loads(response)

    # Pass the list to the template for rendering
    return render_template('records.html', records=list_of_dicts)


@app.route('/create', methods=['POST', 'GET'])
def create():
    # If the method is GET, return the rendered template.
    if request.method == 'GET':
        return render_template('create.html')
    # If the method is POST, Get the form data.
    if request.method == 'POST':
        location = request.form['location']
        address = request.form['address']
        description = request.form['description']
        # Create a dictionary from the form data.
        new_record = {'location': location, 'address': address, 'description': description}
        # Send a request to your deployed CreateRecord function to create the record.
        response = requests.post('https://unhcampusdirections.azurewebsites.net/api/createrecord', json=new_record).text
        # Redirect to view all records.
        # use url_for to redirect to the records route
        return redirect(url_for('records'))


@app.route('/route', methods=['GET', 'POST'])
def route():
    # Fetch the location data from the API
    if request.method == 'GET':
        # Fetch the records
        response = requests.get('https://unhcampusdirections.azurewebsites.net/api/readrecords').text
        list_of_dicts = json_util.loads(response)

        # Pass the records to the template
        return render_template('route.html', records=list_of_dicts)
    elif request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        waypoints = request.form.getlist('waypoints')
        waypoints_str = ';'.join(waypoints)
        travel_mode = request.form['travel_mode']

        return redirect(url_for('show_map', start=start, end=end, waypoints=waypoints_str))

@app.route('/contact')
def contact():
    return render_template('contact.html')
