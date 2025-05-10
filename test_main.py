import pytest
from fastapi.testclient import TestClient
from main import app

# Create a test client
client = TestClient(app)

def test_read_root():
    """
    Test that the root endpoint returns a 200 status code and HTML content
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Welcome to Test-Bot" in response.text

def test_welcome_api():
    """
    Test that the welcome API endpoint returns the correct message
    """
    response = client.get("/api/welcome")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "Features will add soon !!!" == data["message"]

def test_static_files():
    """
    Test that static files are properly mounted
    """
    response = client.get("/static/css/styles.css")
    assert response.status_code == 200
    assert "text/css" in response.headers["content-type"]

@pytest.mark.parametrize(
    "endpoint,expected_status",
    [
        ("/", 200),
        ("/api/welcome", 200),
        ("/nonexistent", 404),
    ],
)
def test_endpoints_status(endpoint, expected_status):
    """
    Test various endpoints for expected status codes
    """
    response = client.get(endpoint)
    assert response.status_code == expected_status
