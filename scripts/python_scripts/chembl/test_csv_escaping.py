#!/usr/bin/env python3
"""
Test CSV field escaping utility
"""

import csv
import io
import sys
import os

# Add parent directory to path to import the utility
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def escape_csv_field_proper(field):
    """
    Properly escape a field for CSV format following RFC 4180 standard.

    CSV standard rules:
    - Fields containing commas, quotes, or newlines must be enclosed in double quotes
    - Double quotes within a field must be escaped by doubling them
    - None/null values become empty strings
    """
    if field is None:
        return ""

    field_str = str(field)

    # Check if field needs quoting
    needs_quoting = any(char in field_str for char in [',', '"', '\n', '\r'])

    if needs_quoting or field_str.strip() != field_str:  # Also quote if has leading/trailing spaces
        # Escape any existing double quotes by doubling them
        field_str = field_str.replace('"', '""')
        # Enclose in double quotes
        return f'"{field_str}"'

    return field_str


def test_csv_escaping():
    """Test various CSV escaping scenarios"""
    print("Testing CSV Field Escaping")
    print("=" * 50)

    test_cases = [
        # (input, expected_output, description)
        ("simple text", "simple text", "Simple text without special chars"),
        ("text with, comma", '"text with, comma"', "Text with comma"),
        ('text with "quotes"', '"text with ""quotes"""', "Text with double quotes"),
        ("text with\nnewline", '"text with\nnewline"', "Text with newline"),
        ("", "", "Empty string"),
        (None, "", "None value"),
        ("  leading space", '"  leading space"', "Leading whitespace"),
        ("trailing space  ", '"trailing space  "', "Trailing whitespace"),
        ('mix, of "special" chars\nhere', '"mix, of ""special"" chars\nhere"', "Multiple special characters"),
        ("Drug treats cancer, inflammation, and pain", '"Drug treats cancer, inflammation, and pain"', "Medical indications with commas"),
        ('Warning: "Black Box" - serious adverse effects', '"Warning: ""Black Box"" - serious adverse effects"', "Drug warning with quotes"),
        ("IC50 = 0.5 µM, Ki = 1.2 nM", '"IC50 = 0.5 µM, Ki = 1.2 nM"', "Bioactivity data with commas"),
    ]

    passed = 0
    failed = 0

    for input_val, expected, description in test_cases:
        result = escape_csv_field_proper(input_val)

        if result == expected:
            print(f"✅ PASS: {description}")
            print(f"   Input: {repr(input_val)}")
            print(f"   Output: {repr(result)}")
            passed += 1
        else:
            print(f"❌ FAIL: {description}")
            print(f"   Input: {repr(input_val)}")
            print(f"   Expected: {repr(expected)}")
            print(f"   Got: {repr(result)}")
            failed += 1
        print()

    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")

    return failed == 0


def test_csv_roundtrip():
    """Test that escaped fields can be properly parsed by Python's CSV module"""
    print("\nTesting CSV Roundtrip (write and read back)")
    print("=" * 50)

    # Test data that might appear in ChemBL
    test_data = [
        ["CHEMBL25", "ASPIRIN", "Anti-inflammatory, analgesic", 'Warning: "GI bleeding risk"'],
        ["CHEMBL520", "COMPOUND X", "Treats cancer, reduces inflammation", "IC50 = 0.5 µM, Ki = 1.2 nM"],
        ["CHEMBL11", "IMIPRAMINE", "Tricyclic\nantidepressant", "Multiple, serious warnings"],
    ]

    # Write using our escaping function
    output = []
    for row in test_data:
        escaped_row = [escape_csv_field_proper(field) for field in row]
        output.append(','.join(escaped_row))

    csv_content = '\n'.join(output)

    print("Generated CSV:")
    print(csv_content)
    print()

    # Read back using Python's CSV module
    csv_file = io.StringIO(csv_content)
    reader = csv.reader(csv_file)

    read_data = list(reader)

    # Compare
    print("Verification:")
    all_match = True
    for i, (original, read_back) in enumerate(zip(test_data, read_data)):
        match = original == read_back
        status = "✅" if match else "❌"
        print(f"{status} Row {i+1}: {'Match' if match else 'Mismatch'}")

        if not match:
            all_match = False
            print(f"   Original: {original}")
            print(f"   Read back: {read_back}")

    return all_match


def test_existing_utility():
    """Test the existing escape_csv_field function if it exists"""
    print("\nTesting Existing Utility Function")
    print("=" * 50)

    try:
        from src.utils.escape_csv_field import escape_csv_field

        # Test basic cases
        test_cases = [
            ("simple", "Simple text"),
            ("with, comma", "Text with comma"),
            ("with \"quotes\"", "Text with quotes"),
        ]

        print("Testing existing escape_csv_field function:")
        for test_val, description in test_cases:
            try:
                result = escape_csv_field(test_val)
                print(f"   {description}: {repr(test_val)} -> {repr(result)}")
            except Exception as e:
                print(f"   ❌ Error with {repr(test_val)}: {e}")

    except ImportError as e:
        print(f"❌ Could not import existing utility: {e}")
    except SyntaxError as e:
        print(f"❌ Syntax error in existing utility: {e}")
        print("   The existing file needs to be fixed")


if __name__ == "__main__":
    # Run tests
    print("CSV Escaping Utility Test Suite")
    print("=" * 50)

    # Test our proper implementation
    escaping_passed = test_csv_escaping()

    # Test roundtrip
    roundtrip_passed = test_csv_roundtrip()

    # Try to test existing utility
    test_existing_utility()

    # Summary
    print("\n" + "=" * 50)
    print("FINAL SUMMARY")
    print("=" * 50)

    if escaping_passed and roundtrip_passed:
        print("✅ All CSV escaping tests passed!")
        print("\nRecommendation: Fix the existing utility file with the proper implementation")
    else:
        print("⚠️  Some tests failed - review the CSV escaping implementation")