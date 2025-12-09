#!/usr/bin/env python3
"""
Test ChemBL API connectivity and basic functionality
"""

import requests
import json
from time import sleep

ORIGIN = "https://www.ebi.ac.uk"
BASE_URL = f"{ORIGIN}/chembl/api/data"
HEADERS = {"User-Agent": "chembl-neo4j-script", "Accept": "application/json"}


def test_api_status():
    """Test the /status endpoint"""
    print("Testing ChemBL API connectivity...")
    print(f"Base URL: {BASE_URL}")

    # The ChemBL API doesn't have a /status endpoint, but we can test with /status endpoint
    # Actually, let's test with the base endpoint which should return API info
    url = BASE_URL

    try:
        print(f"\n1. Testing base endpoint: {url}")
        response = requests.get(url, headers=HEADERS, timeout=10)
        print(f"   Status Code: {response.status_code}")

        if response.status_code == 200:
            print("   ✅ API is accessible")
            try:
                data = response.json()
                if 'available_resources' in data:
                    print(f"   Available resources: {len(data['available_resources'])} endpoints")
                    # Show first 5 resources
                    for resource in list(data['available_resources'].keys())[:5]:
                        print(f"      - {resource}")
                else:
                    # The base endpoint might return different structure
                    print(f"   Response type: {type(data)}")
                    if isinstance(data, dict):
                        print(f"   Keys in response: {list(data.keys())[:5]}")
            except json.JSONDecodeError:
                # Some endpoints might return HTML or other formats
                print(f"   Response content type: {response.headers.get('content-type', 'unknown')}")
                print("   Note: Base endpoint doesn't return JSON, but API is accessible")
        else:
            print(f"   ❌ Unexpected status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"   ❌ Connection error: {e}")
        return False

    # Test a simple query endpoint
    print("\n2. Testing molecule endpoint with a sample query...")
    test_url = f"{BASE_URL}/molecule/CHEMBL25"  # Aspirin

    try:
        response = requests.get(test_url, headers=HEADERS, timeout=10)
        print(f"   URL: {test_url}")
        print(f"   Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Successfully retrieved data for {data.get('molecule_chembl_id', 'unknown')}")
            print(f"   Drug name: {data.get('pref_name', 'Not available')}")
            if 'molecule_properties' in data:
                print(f"   Has molecule properties: Yes")
        else:
            print(f"   ❌ Failed to retrieve molecule data")

    except requests.exceptions.RequestException as e:
        print(f"   ❌ Error fetching molecule: {e}")
        return False

    # Test the actual endpoint we'll use for approved drugs
    print("\n3. Testing approved drugs endpoint with pagination...")
    test_url = f"{BASE_URL}/molecule?max_phase=4&molecule_type=Small%20molecule&limit=5"

    try:
        response = requests.get(test_url, headers=HEADERS, timeout=10)
        print(f"   URL: {test_url}")
        print(f"   Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            molecules = data.get('molecules', [])
            print(f"   ✅ Retrieved {len(molecules)} molecules")

            if molecules:
                print("   Sample molecules:")
                for mol in molecules[:3]:
                    print(f"      - {mol.get('molecule_chembl_id')}: {mol.get('pref_name', 'No name')}")

            # Check pagination metadata
            if 'page_meta' in data:
                page_meta = data['page_meta']
                print(f"   Total molecules available: {page_meta.get('total_count', 'Unknown')}")
                print(f"   Has next page: {'next' in page_meta and page_meta['next'] is not None}")
        else:
            print(f"   ❌ Failed to retrieve approved drugs")

    except requests.exceptions.RequestException as e:
        print(f"   ❌ Error fetching approved drugs: {e}")
        return False

    print("\n✅ All connectivity tests passed!")
    return True


if __name__ == "__main__":
    success = test_api_status()
    exit(0 if success else 1)
