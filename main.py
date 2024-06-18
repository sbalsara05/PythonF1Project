import os
import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

# Setup Plotting
plotting.setup_mpl()

# Check if cache directory exists, if not, create it
if not os.path.exists('cache'):
    os.makedirs('cache')

# Enable Cache
ff1.Cache.enable_cache('cache')

# Load Session Data
race1 = ff1.get_session(2021, 'Monza', 'R')

# Collect all race laps
race1.load(telemetry=True, laps=True)
session_laps = race1.laps

# Debug: Check if session_laps is loaded correctly
print(f"Loaded laps: {session_laps}")

# Get laps of Drivers
laps_bot = session_laps.pick_drivers("BOT")
laps_ham = session_laps.pick_drivers("HAM")

# Debug: Check if laps are correctly filtered
print(f"Laps for BOT: {laps_bot}")
print(f"Laps for HAM: {laps_ham}")

# Extract the fastest laps
fastest_bot = laps_bot.pick_fastest()
fastest_ham = laps_ham.pick_fastest()

# Debug: Check if fastest laps are correctly extracted
print(f"Fastest lap for BOT: {fastest_bot}")
print(f"Fastest lap for HAM: {fastest_ham}")

# Get Telemetry from the Fastest Laps
telemetry_bot = fastest_bot.get_car_data().add_distance()
telemetry_ham = fastest_ham.get_car_data().add_distance()

# Debug: Check if telemetry data is correctly processed
print(f"Telemetry for BOT: {telemetry_bot}")
print(f"Telemetry for HAM: {telemetry_ham}")

# Plot Data
fig, ax = plt.subplots(3)
fig.suptitle("Fastest Race Lap Telemetry Comparison")

ax[0].plot(telemetry_bot['Distance'], telemetry_bot['Speed'], label='BOT')
ax[0].plot(telemetry_ham['Distance'], telemetry_ham['Speed'], label='HAM')
ax[0].set(ylabel='Speed')
ax[0].legend(loc="lower right")
ax[1].plot(telemetry_bot['Distance'], telemetry_bot['Throttle'], label='BOT')
ax[1].plot(telemetry_ham['Distance'], telemetry_ham['Throttle'], label='HAM')
ax[1].set(ylabel='Throttle')
ax[2].plot(telemetry_bot['Distance'], telemetry_bot['Brake'], label='BOT')
ax[2].plot(telemetry_ham['Distance'], telemetry_ham['Brake'], label='HAM')
ax[2].set(ylabel='Brakes')

# Hide x labels and tick labels for top plots and y ticks for right plots
for a in ax.flat:
    a.label_outer()

plt.show()
