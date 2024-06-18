import fastf1 as ff1
from fastf1 import plotting

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

# Setup Plotting
plotting.setup_mpl()

# Enable Cache
ff1.Cache.enable_cache('cache')

# Load Session Data
race1 = ff1.get_session(2021, "Zandvoort", "R")

# Collect all race laps
laps = race1.load(telemetry=True)

# Get laps of Drivers
laps_bot = laps.pick_driver("BOT")
laps_ham = laps.pick_driver('HAM')

# Extract the fastest laps
fastest_bot = laps_bot.pick_fastest()
fastest_ham = laps_ham.pick_fastest()

# Get Telemetry from the Fastest Laps
telemetry_bot = fastest_bot.get_car_data().add_distance()
telemetry_ham = fastest_ham.get_car_data().add_distance()

