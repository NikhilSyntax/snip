
# Import FastAPI's testing tool
from fastapi.testclient import TestClient

# Import our actual FastAPI application
from app.main import app


# Create a test client using our application
client = TestClient(app)


# Our first automated test
def test_health_check():

    # Send a GET request to /health
    response = client.get("/health")

    # Check whether the HTTP status code is 200 (success)
    assert response.status_code == 200

    # Check whether the returned JSON matches what we expect
    assert response.json() == {
        "status": "healthy",
        "service": "snip-api",
    }
