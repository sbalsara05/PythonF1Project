import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    with app.test_client() as client:
        yield client

def test_telemetry_endpoint(client):
    """Test the /telemetry endpoint."""

    # Test case 1: Valid request with correct parameters
    response = client.get('/telemetry?year=2023&event_name=Monaco&session_type=race&driver1=BOT&driver2=HAM')
    assert response.status_code == 400
    data = response.get_json()
    assert 'year' in data
    assert 'event_name' in data
    assert 'session_type' in data
    assert 'telemetry_data' in data
    assert 'BOT' in data['telemetry_data']
    assert 'HAM' in data['telemetry_data']

    # Test case 2: Missing required parameter (session_type)
    response = client.get('/telemetry?year=2023&event_name=Monaco&driver1=BOT&driver2=HAM')
    assert response.status_code == 400
    assert b"Bad Request" in response.data

    # Test case 3: Invalid year (not an integer)
    response = client.get('/telemetry?year=twentytwentythree&event_name=Monaco&session_type=race&driver1=BOT&driver2=HAM')
    assert response.status_code == 400
    assert b"Bad Request" in response.data

    # Test case 4: Invalid driver identifier
    response = client.get('/telemetry?year=2023&event_name=Monaco&session_type=race&driver1=XYZ&driver2=HAM')
    assert response.status_code == 400
    assert b"Bad Request" in response.data
