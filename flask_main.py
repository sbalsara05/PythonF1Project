import os
import fastf1 as ff1
from fastf1 import plotting
from flask import Flask, request, jsonify

# Setup Plotting
plotting.setup_mpl()

# Check if cache directory exists, if not, create it
if not os.path.exists('cache'):
    os.makedirs('cache')

# Enable Cache
ff1.Cache.enable_cache('cache')

# Initialize Flask app
app = Flask(__name__)

# Define driver colors
driver_colors = {
    "BOT": "Blue",
    "HAM": "Purple",
    "VET": "Red",
    "LEC": "white",
    "VER": "#D95319",  # Orange
    "PER": "yellow",
    "NOR": "#BFFE08",  # Neon Yellow
    "SAI": "#666B64",  # Pewter or something
    "STR": "#004225",  # AMR Brit. Racing Green
    "ALO": "#7dd9ff",  # Mild Seven Blue
    "MSC": "#7BEA05",  # Lime Green
    "MAZ": "#EAA305",  # Slightly lighter orange
    "GAS": "#181756",  # Dark Blue
    "TSU": "Red",
    "LAT": "#000000",  # Black
    "RUS": "#37a4ee",  # Blue from Russell's Helmet
    "RAI": "#86995B",  # Lotus Gold
    "GIO": "#009246",  # Italian Flag Green
    "OCO": "#F363B9",  # BWT Pink
    "RIC": "#94d0d2",  # Color from 2021 Helmet
    "ZHO": "#52E252",  # Kick Sauber Green
    "SAR": "64C4FF",   # Williams Blue
    "ALB": "#FF98E5",  # Pink from 2024 Helmet
    # Add more drivers and colors as needed
}

@app.route('/telemetry', methods=['GET'])
def get_telemetry():
    year = int(request.args.get('year'))
    event_name = request.args.get('event_name')
    session_type = request.args.get('session_type')
    driver1 = request.args.get('driver1').upper()
    driver2 = request.args.get('driver2').upper()

    # Load Session Data
    race1 = ff1.get_session(year, event_name, session_type)
    race1.load(telemetry=True, laps=True)
    session_laps = race1.laps

    # Extract the fastest laps and telemetry data for each driver
    telemetry_data = {}

    for driver in [driver1, driver2]:
        laps = session_laps.pick_drivers(driver)
        fastest_lap = laps.pick_fastest()
        telemetry = fastest_lap.get_car_data().add_distance()
        telemetry_data[driver] = {
            'Distance': telemetry['Distance'].tolist(),
            'Speed': telemetry['Speed'].tolist(),
            'Throttle': telemetry['Throttle'].tolist(),
            'Brake': telemetry['Brake'].tolist(),
            'Color': driver_colors.get(driver, 'Black')
        }

    return jsonify({
        'year': year,
        'event_name': event_name,
        'session_type': session_type,
        'telemetry_data': telemetry_data
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080, use_reloader=False)