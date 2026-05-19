"""
API Integration & JSON Handling Project

Developed by: BODABANDA SRINATH
Role: Python Developer Intern

Features:
1. Fetch data from API
2. Parse JSON response
3. Search/filter user data
4. Handle API errors
"""

# Import requests module
import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users"

try:
    # Send GET request to API
    response = requests.get(url)

    # Check if request is successful
    response.raise_for_status()

    # Convert JSON response into Python data
    users = response.json()

    print("API Data Fetched Successfully!\n")

    # -------------------------------
    # Display User Information
    # -------------------------------

    for user in users:
        print("ID:", user["id"])
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("City:", user["address"]["city"])
        print("-" * 40)

    # -------------------------------
    # Search Logic
    # -------------------------------

    search_name = input("\nEnter name to search: ").lower()

    found = False

    for user in users:
        if search_name in user["name"].lower():
            print("\nUser Found!")
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("Company:", user["company"]["name"])
            found = True

    if not found:
        print("No user found with that name.")

# -------------------------------
# Error Handling
# -------------------------------

except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)

except requests.exceptions.ConnectionError:
    print("Connection Error. Check internet connection.")

except requests.exceptions.Timeout:
    print("Request Timeout.")

except requests.exceptions.RequestException as err:
    print("Something went wrong:", err)