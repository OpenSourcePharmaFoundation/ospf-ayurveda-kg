#!/usr/bin/env python3
"""
Test pagination handling for ChemBL API
"""

import requests
import time
from typing import List, Dict, Optional

ORIGIN = "https://www.ebi.ac.uk"
BASE_URL = f"{ORIGIN}/chembl/api/data"
HEADERS = {"User-Agent": "chembl-neo4j-script", "Accept": "application/json"}


def test_basic_pagination():
    """Test basic pagination with approved drugs endpoint"""
    print("Testing basic pagination with approved drugs")
    print("=" * 50)

    url = f"{BASE_URL}/molecule"
    params = {
        "max_phase": 4,
        "molecule_type": "Small molecule",
        "limit": 10,
        "offset": 0
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)

        if response.status_code == 200:
            data = response.json()

            # Check for expected pagination structure
            print("✅ First page retrieved successfully")
            print(f"   Total compounds available: {data.get('page_meta', {}).get('total_count', 'Unknown')}")
            print(f"   Current page limit: {data.get('page_meta', {}).get('limit', 'Unknown')}")
            print(f"   Current offset: {data.get('page_meta', {}).get('offset', 'Unknown')}")

            molecules = data.get('molecules', [])
            print(f"   Molecules on this page: {len(molecules)}")

            # Check pagination metadata
            page_meta = data.get('page_meta', {})
            if 'next' in page_meta and page_meta['next']:
                print("   ✅ Next page URL exists")
                print(f"   Next page: {page_meta['next'][:100]}...")

            if 'previous' in page_meta:
                print(f"   Previous page: {page_meta.get('previous', 'None')}")

            return True
        else:
            print(f"❌ Failed to retrieve first page: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_multiple_pages(num_pages=3):
    """Test fetching multiple pages sequentially"""
    print("\nTesting multiple page fetching")
    print("=" * 50)

    all_molecules = []
    limit = 5

    for page in range(num_pages):
        offset = page * limit
        print(f"\nFetching page {page + 1}/{num_pages} (offset={offset}, limit={limit})")

        url = f"{BASE_URL}/molecule"
        params = {
            "max_phase": 4,
            "molecule_type": "Small molecule",
            "limit": limit,
            "offset": offset
        }

        try:
            response = requests.get(url, params=params, headers=HEADERS, timeout=10)

            if response.status_code == 200:
                data = response.json()
                molecules = data.get('molecules', [])
                all_molecules.extend(molecules)

                print(f"   ✅ Retrieved {len(molecules)} molecules")

                # Show first molecule from each page
                if molecules:
                    first_mol = molecules[0]
                    print(f"   First molecule: {first_mol.get('molecule_chembl_id')} - {first_mol.get('pref_name', 'No name')}")

                # Rate limiting between pages
                if page < num_pages - 1:
                    print("   Waiting 0.5s before next page...")
                    time.sleep(0.5)
            else:
                print(f"   ❌ Failed to retrieve page {page + 1}: {response.status_code}")

        except Exception as e:
            print(f"   ❌ Error on page {page + 1}: {e}")

    print(f"\n{'='*50}")
    print(f"Total molecules collected across {num_pages} pages: {len(all_molecules)}")

    # Check for duplicates
    chembl_ids = [mol.get('molecule_chembl_id') for mol in all_molecules]
    unique_ids = set(chembl_ids)

    if len(chembl_ids) == len(unique_ids):
        print("✅ No duplicate molecules found - pagination working correctly")
    else:
        print(f"⚠️  Found {len(chembl_ids) - len(unique_ids)} duplicate molecules")

    return len(all_molecules) == num_pages * limit


def test_pagination_consistency():
    """Test that pagination returns consistent results"""
    print("\nTesting pagination consistency")
    print("=" * 50)

    # Fetch same page twice to ensure consistency
    url = f"{BASE_URL}/molecule"
    params = {
        "max_phase": 4,
        "molecule_type": "Small molecule",
        "limit": 5,
        "offset": 10
    }

    print("Fetching same page twice to check consistency...")

    try:
        # First request
        response1 = requests.get(url, params=params, headers=HEADERS, timeout=10)
        data1 = response1.json()
        molecules1 = data1.get('molecules', [])
        ids1 = [mol.get('molecule_chembl_id') for mol in molecules1]

        time.sleep(0.5)  # Small delay between requests

        # Second request
        response2 = requests.get(url, params=params, headers=HEADERS, timeout=10)
        data2 = response2.json()
        molecules2 = data2.get('molecules', [])
        ids2 = [mol.get('molecule_chembl_id') for mol in molecules2]

        if ids1 == ids2:
            print("✅ Pagination returns consistent results")
            print(f"   Both requests returned: {', '.join(ids1[:3])}...")
            return True
        else:
            print("⚠️  Pagination returned different results!")
            print(f"   First request: {ids1}")
            print(f"   Second request: {ids2}")
            return False

    except Exception as e:
        print(f"❌ Error testing consistency: {e}")
        return False


def test_edge_cases():
    """Test edge cases in pagination"""
    print("\nTesting pagination edge cases")
    print("=" * 50)

    # Test 1: Very large offset
    print("\n1. Testing very large offset (should return empty)...")
    url = f"{BASE_URL}/molecule"
    params = {
        "max_phase": 4,
        "molecule_type": "Small molecule",
        "limit": 10,
        "offset": 100000  # Way beyond total count
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            molecules = data.get('molecules', [])
            if len(molecules) == 0:
                print("   ✅ Large offset correctly returns empty result")
            else:
                print(f"   ⚠️  Expected empty result, got {len(molecules)} molecules")
    except Exception as e:
        print(f"   ❌ Error: {e}")

    time.sleep(0.5)

    # Test 2: Zero limit (should use default or error)
    print("\n2. Testing zero limit...")
    params = {
        "max_phase": 4,
        "molecule_type": "Small molecule",
        "limit": 0,
        "offset": 0
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            molecules = data.get('molecules', [])
            print(f"   Result: Got {len(molecules)} molecules")
            if len(molecules) == 0:
                print("   ✅ Zero limit handled correctly")
        else:
            print(f"   Status code: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

    time.sleep(0.5)

    # Test 3: Maximum limit
    print("\n3. Testing maximum limit (1000)...")
    params = {
        "max_phase": 4,
        "molecule_type": "Small molecule",
        "limit": 1000,  # ChemBL typically caps at 1000
        "offset": 0
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            molecules = data.get('molecules', [])
            actual_limit = data.get('page_meta', {}).get('limit')
            print(f"   Requested limit: 1000")
            print(f"   Actual limit returned: {actual_limit}")
            print(f"   Molecules returned: {len(molecules)}")
            if len(molecules) <= 1000:
                print("   ✅ Maximum limit handled correctly")
        else:
            print(f"   Status code: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Error: {e}")


if __name__ == "__main__":
    print("ChemBL API Pagination Test")
    print("=" * 50)

    # Run all tests
    tests_passed = []

    print("\nTest 1: Basic Pagination")
    print("-" * 50)
    tests_passed.append(test_basic_pagination())

    print("\n\nTest 2: Multiple Pages")
    print("-" * 50)
    tests_passed.append(test_multiple_pages(num_pages=3))

    print("\n\nTest 3: Pagination Consistency")
    print("-" * 50)
    tests_passed.append(test_pagination_consistency())

    print("\n\nTest 4: Edge Cases")
    print("-" * 50)
    test_edge_cases()  # Edge cases don't return boolean

    # Final summary
    print("\n" + "=" * 50)
    print("FINAL SUMMARY")
    print("=" * 50)

    if all(tests_passed):
        print("✅ All pagination tests passed!")
        print("Pagination is working correctly for data collection")
    else:
        print("⚠️  Some pagination tests failed")
        print("Review the implementation before proceeding with full data collection")