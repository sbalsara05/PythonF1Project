import os
import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt

# Setup Plotting
plotting.setup_mpl()

# Check if cache directory exists, if not, create it
if not os.path.exists('cache'):
    os.makedirs('cache')

# Enable Cache
ff1.Cache.enable_cache('cache')


# Function to fetch telemetry data
def fetch_telemetry_data(year, event_name, session_type, driver1, driver2):
    race = ff1.get_session(year, event_name, session_type)
    race.load(telemetry=True, laps=True)
    session_laps = race.laps

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
        }

    return telemetry_data
