import json
import time
import os


# this is the example "main" program
def response_data():

    print("Listening...")

    # continuously check if response_data.json file exists
    while not os.path.exists('response_data.json'):
        time.sleep(1)

    try:
        # open JSON file for reading
        with open('response_data.json', 'r') as f:
            data = json.load(f)
            if data:
                print("Filtered dataset:", data)
            else:
                print("No data matches the given criteria. Please try again.")

    except FileNotFoundError:
        print("No file found.")


response_data()
