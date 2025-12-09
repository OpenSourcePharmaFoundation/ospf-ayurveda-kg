#!/usr/bin/env python3
"""
Test rate limiting for ChemBL API requests
"""

import requests
import time
from datetime import datetime

ORIGIN = "https://www.ebi.ac.uk"
BASE_URL = f"{ORIGIN}/chembl/api/data"
HEADERS = {"User-Agent": "chembl-neo4j-script", "Accept": "application/json"}


def test_rate_limiting(num_requests=5, delay_seconds=0.5):
    """
    Test rate limiting by making multiple requests with specified delay

    Args:
        num_requests: Number of requests to make
        delay_seconds: Delay between requests in seconds
    """
    print(f"Testing rate limiting with {num_requests} requests")
    print(f"Delay between requests: {delay_seconds} seconds")
    print("-" * 50)

    # Test with simple molecule queries - all verified to exist
    chembl_ids = ["CHEMBL25", "CHEMBL1", "CHEMBL520", "CHEMBL11", "CHEMBL14"]  # Aspirin, Epinephrine, Xanthene, Imipramine, Carbachol

    request_times = []
    successful_requests = 0
    failed_requests = 0

    for i, chembl_id in enumerate(chembl_ids[:num_requests]):
        start_time = time.time()
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]

        url = f"{BASE_URL}/molecule/{chembl_id}"

        try:
            print(f"\n[{timestamp}] Request {i+1}/{num_requests}")
            print(f"   Fetching: {chembl_id}")

            response = requests.get(url, headers=HEADERS, timeout=10)

            if response.status_code == 200:
                data = response.json()
                drug_name = data.get('pref_name', 'Unknown')
                print(f"   ✅ Success: {drug_name}")
                successful_requests += 1
            elif response.status_code == 429:
                print(f"   ⚠️  Rate limited! Status: {response.status_code}")
                failed_requests += 1
            else:
                print(f"   ❌ Error: Status {response.status_code}")
                failed_requests += 1

        except requests.exceptions.RequestException as e:
            print(f"   ❌ Request failed: {e}")
            failed_requests += 1

        request_time = time.time() - start_time
        request_times.append(request_time)
        print(f"   Request time: {request_time:.3f}s")

        # Apply rate limiting delay (except for last request)
        if i < num_requests - 1:
            print(f"   Waiting {delay_seconds}s before next request...")
            time.sleep(delay_seconds)

    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Total requests: {num_requests}")
    print(f"Successful: {successful_requests}")
    print(f"Failed: {failed_requests}")
    print(f"Average request time: {sum(request_times)/len(request_times):.3f}s")
    print(f"Total time: {sum(request_times) + delay_seconds * (num_requests - 1):.3f}s")

    if failed_requests == 0:
        print("\n✅ Rate limiting test passed - no requests were rejected")
    else:
        print(f"\n⚠️  {failed_requests} requests were rate limited or failed")

    return successful_requests == num_requests


def test_without_rate_limiting(num_requests=10):
    """
    Test what happens without rate limiting (rapid fire requests)
    """
    print("\nTesting WITHOUT rate limiting (rapid requests)")
    print("=" * 50)

    successful = 0
    rate_limited = 0

    for i in range(num_requests):
        url = f"{BASE_URL}/molecule/CHEMBL{25 + i}"

        try:
            response = requests.get(url, headers=HEADERS, timeout=5)
            if response.status_code == 200:
                successful += 1
                print(f"Request {i+1}: ✅ Success")
            elif response.status_code == 429:
                rate_limited += 1
                print(f"Request {i+1}: ⚠️  Rate limited!")
            else:
                print(f"Request {i+1}: ❌ Error {response.status_code}")
        except Exception as e:
            print(f"Request {i+1}: ❌ Failed - {e}")

    print(f"\nResults: {successful} successful, {rate_limited} rate limited")

    if rate_limited > 0:
        print("⚠️  API enforces rate limiting - delays are necessary!")
    else:
        print("✅ No rate limiting detected for rapid requests")

    return rate_limited == 0


if __name__ == "__main__":
    print("ChemBL API Rate Limiting Test")
    print("=" * 50)

    # Test 1: With proper rate limiting (0.5s delay)
    print("\nTest 1: WITH rate limiting (0.5s delay)")
    print("-" * 50)
    test1_passed = test_rate_limiting(num_requests=5, delay_seconds=0.5)

    time.sleep(2)  # Wait before next test

    # Test 2: With slower rate limiting (1s delay)
    print("\n\nTest 2: WITH rate limiting (1s delay)")
    print("-" * 50)
    test2_passed = test_rate_limiting(num_requests=3, delay_seconds=1.0)

    time.sleep(2)  # Wait before next test

    # Test 3: Without rate limiting (rapid requests)
    # Note: We'll do fewer requests to be respectful
    print("\n\nTest 3: Testing rapid requests (no delay)")
    print("-" * 50)
    no_rate_limit_issues = test_without_rate_limiting(num_requests=5)

    # Final summary
    print("\n" + "=" * 50)
    print("FINAL RESULTS")
    print("=" * 50)
    print(f"Test 1 (0.5s delay): {'✅ PASSED' if test1_passed else '❌ FAILED'}")
    print(f"Test 2 (1.0s delay): {'✅ PASSED' if test2_passed else '❌ FAILED'}")
    print(f"Test 3 (no delay): {'✅ No rate limiting' if no_rate_limit_issues else '⚠️  Rate limiting detected'}")

    if test1_passed and test2_passed:
        print("\n✅ Rate limiting implementation verified!")
        print("Recommended delay: 0.5-1.0 seconds between requests")
    else:
        print("\n⚠️  Some tests failed - review rate limiting implementation")