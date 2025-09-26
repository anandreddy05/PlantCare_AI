#!/usr/bin/env python3
"""
Test script to verify crop prediction APIs are working.
"""

import requests
import json

def test_crop_recommendation():
    """Test crop recommendation API."""
    url = "http://localhost:5000/api/crop-predictions/recommend-crop"
    data = {
        "N": 90,
        "P": 42,
        "K": 43,
        "temperature": 20.87,
        "humidity": 82.0,
        "ph": 6.5,
        "rainfall": 202.9
    }
    
    try:
        response = requests.post(url, json=data)
        print(f"Crop Recommendation API Test:")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error testing crop recommendation: {e}")
        return False

def test_yield_prediction():
    """Test yield prediction API."""
    url = "http://localhost:5000/api/crop-predictions/predict-yield"
    data = {
        "Crop": "Rice",
        "Season": "Kharif",
        "State": "Punjab",
        "Annual_Rainfall": 1000.0,
        "Fertilizer": 100.0,
        "Pesticide": 50.0
    }
    
    try:
        response = requests.post(url, json=data)
        print(f"\nYield Prediction API Test:")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error testing yield prediction: {e}")
        return False

def test_crop_options():
    """Test crop options API."""
    url = "http://localhost:5000/api/crop-predictions/crop-options"
    
    try:
        response = requests.get(url)
        print(f"\nCrop Options API Test:")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error testing crop options: {e}")
        return False

if __name__ == "__main__":
    print("🌱 Testing Crop Prediction APIs\n")
    
    # Test all endpoints
    tests = [
        test_crop_recommendation,
        test_yield_prediction,
        test_crop_options
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print(f"\n📊 Test Results: {sum(results)}/{len(results)} passed")
    
    if all(results):
        print("✅ All crop prediction APIs are working correctly!")
    else:
        print("❌ Some tests failed. Check the server logs.")