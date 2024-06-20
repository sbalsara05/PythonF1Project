# import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from telemetry import fetch_telemetry_data  # Import the function from your main.py

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

# Define driver colors (if needed)
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

# Define route for /telemetry endpoint
@app.route('/telemetry', methods=['GET'])
def get_telemetry():
    try:
        # Extract parameters from query string
        year = int(request.args.get('year'))
        event_name = request.args.get('event_name')
        session_type = request.args.get('session_type')
        driver1 = request.args.get('driver1').upper()
        driver2 = request.args.get('driver2').upper()

        # Fetch telemetry data using function from main.py
        telemetry_data = fetch_telemetry_data(year, event_name, session_type, driver1, driver2)

        # Prepare response
        return jsonify({
            'year': year,
            'event_name': event_name,
            'session_type': session_type,
            'telemetry_data': telemetry_data
        })

    except Exception as e:
        # Handle exceptions
        return jsonify({'error': str(e)}), 500

# Run the Flask application if executed directly
if __name__ == '__main__':
    app.run(debug=True, port=8080)
