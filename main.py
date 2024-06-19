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

# Load Session Data
year = int(input("Enter Year: \n"))
event_name = input("Enter Race: (i.e. Monza): \n")
session_type = input("Enter Session Type (Race, Qualifying, etc.):\n")

race1 = ff1.get_session(year, event_name, session_type)

# Collect all race laps
race1.load(telemetry=True, laps=True)
session_laps = race1.laps

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

# Function to get valid driver input from user
def get_valid_driver_input():
    while True:
        driver_input = input("Enter a driver identifier (e.g., BOT, HAM, VET, etc.): ").strip().upper()
        if driver_input in driver_colors:
            return driver_input
        else:
            print(f"Driver '{driver_input}' not found. Please enter a valid driver identifier.")

# Get user inputs for drivers
print("Enter the first driver:")
driver1 = get_valid_driver_input().upper()

print("Enter the second driver:")
driver2 = get_valid_driver_input().upper()

# Pick the drivers you want to compare
drivers = [driver1, driver2]

# Extract the fastest laps and telemetry data for each driver
fastest_laps = {}
telemetry_data = {}

for driver in drivers:
    laps = session_laps.pick_drivers(driver)
    fastest_lap = laps.pick_fastest()
    telemetry = fastest_lap.get_car_data().add_distance()
    fastest_laps[driver] = fastest_lap
    telemetry_data[driver] = telemetry

# Plot Data
fig, ax = plt.subplots(3)
fig.suptitle(f"Fastest {session_type} Lap Telemetry Comparison in {year} for {event_name}")

for driver, telemetry in telemetry_data.items():
    color = driver_colors.get(driver, "Black")  # Default to black if color not found
    ax[0].plot(telemetry['Distance'], telemetry['Speed'], label=driver, color=color)
    ax[1].plot(telemetry['Distance'], telemetry['Throttle'], label=driver, color=color)
    ax[2].plot(telemetry['Distance'], telemetry['Brake'], label=driver, color=color)

ax[0].set(ylabel='Speed')
ax[0].legend(loc="lower right")

ax[1].set(ylabel='Throttle')

ax[2].set(ylabel='Brakes')

# Hide x labels and tick labels for top plots and y ticks for right plots
for a in ax.flat:
    a.label_outer()

plt.show()
