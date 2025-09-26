"""
Test script to verify the delete endpoints work correctly
"""
import requests
import json

# Test configuration
BASE_URL = "http://localhost:5000/api/crop-predictions"

def test_endpoints():
    """Test that the delete endpoints are available (will return 401 without auth)"""
    
    # Test recommendation delete endpoint
    response = requests.delete(f"{BASE_URL}/recommendation-history/1")
    print(f"DELETE recommendation endpoint status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Test yield prediction delete endpoint  
    response = requests.delete(f"{BASE_URL}/yield-history/1")
    print(f"DELETE yield prediction endpoint status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Test OPTIONS request to see available methods
    response = requests.options(f"{BASE_URL}/recommendation-history/1")
    print(f"OPTIONS recommendation endpoint status: {response.status_code}")
    if 'Allow' in response.headers:
        print(f"Allowed methods: {response.headers['Allow']}")

if __name__ == "__main__":
    try:
        test_endpoints()
    except requests.exceptions.ConnectionError:
        print("Could not connect to server. Make sure the Flask server is running on localhost:5000")
    except Exception as e:
        print(f"Error: {e}")