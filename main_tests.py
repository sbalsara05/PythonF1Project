import pytest
import fastf1


def test_get_session_data():
    # Load session data (example: 2023 Bahrain Grand Prix, Qualifying)
    session = fastf1.get_session(2023, 'Bahrain', 'Q')

    # Load laps data into session_laps
    session.load()
    session_laps = session.laps

    # Check if session_laps is properly loaded
    assert session_laps is not None, "Failed to load session laps data"

    # Now you can call the pick_drivers method
    laps_bot = session_laps.pick_drivers("BOT")

    # Verify that laps_bot is not None or empty
    assert laps_bot is not None, "Failed to pick driver laps data"
    assert len(laps_bot) > 0, "No laps found for the driver BOT"

    # Optionally print laps_bot for debugging purposes (remove in production)
    print(laps_bot)


if __name__ == "__main__":
    pytest.main()
