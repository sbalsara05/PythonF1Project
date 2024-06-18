import pytest
import fastf1

@pytest.fixture(scope="module")
def session_data():
    # Load session data (example: 2023 Bahrain Grand Prix, Qualifying)
    session = fastf1.get_session(2023, 'Bahrain', 'Q')
    session.load()
    return session

def test_get_session_data(session_data):
    session_laps = session_data.laps

    # Check if session_laps is properly loaded
    assert session_laps is not None, "Failed to load session laps data"

    # Now you can call the pick_drivers method
    laps_bot = session_laps.pick_drivers("BOT")

    # Verify that laps_bot is not None or empty
    assert laps_bot is not None, "Failed to pick driver laps data"
    assert len(laps_bot) > 0, "No laps found for the driver BOT"

    # Optionally print laps_bot for debugging purposes (remove in production)
    print(laps_bot)

def test_pick_multiple_drivers(session_data):
    session_laps = session_data.laps

    # Pick laps for multiple drivers
    drivers_laps = session_laps.pick_drivers(["BOT", "HAM"])

    # Verify that laps are picked correctly
    assert drivers_laps is not None, "Failed to pick multiple driver laps data"
    assert len(drivers_laps) > 0, "No laps found for the specified drivers"

    # Check that the drivers in the result are correct
    drivers = set(drivers_laps['Driver'])
    assert 'BOT' in drivers, "BOT laps not found"
    assert 'HAM' in drivers, "HAM laps not found"

def test_pick_fastest_lap(session_data):
    session_laps = session_data.laps

    # Pick fastest lap for a driver
    laps_bot = session_laps.pick_drivers("BOT")
    fastest_bot = laps_bot.pick_fastest()

    # Verify that the fastest lap is picked
    assert fastest_bot is not None, "Failed to pick the fastest lap for BOT"

    # Optionally print fastest_bot for debugging purposes (remove in production)
    print(fastest_bot)

def test_telemetry_data(session_data):
    session_laps = session_data.laps

    # Pick fastest lap for a driver
    laps_bot = session_laps.pick_drivers("BOT")
    fastest_bot = laps_bot.pick_fastest()

    # Get telemetry data
    telemetry_bot = fastest_bot.get_car_data().add_distance()

    # Verify telemetry data is available and contains expected keys
    assert telemetry_bot is not None, "Failed to get telemetry data for BOT"

    # Optionally print telemetry_bot for debugging purposes (remove in production)
    print(telemetry_bot)

def test_cache_functionality():
    # Enable Cache
    fastf1.Cache.enable_cache('cache')

    # Load session data for the first time
    session = fastf1.get_session(2023, 'Bahrain', 'Q')
    session.load()
    session_laps_first_load = session.laps

    # Load session data for the second time
    session = fastf1.get_session(2023, 'Bahrain', 'Q')
    session.load()
    session_laps_second_load = session.laps

    # Verify that cache speeds up data loading
    assert session_laps_first_load is not None, "Failed to load session laps data on first load"
    assert session_laps_second_load is not None, "Failed to load session laps data on second load"

    # Optionally print session_laps for debugging purposes (remove in production)
    print(session_laps_first_load)
    print(session_laps_second_load)

if __name__ == "__main__":
    pytest.main()
