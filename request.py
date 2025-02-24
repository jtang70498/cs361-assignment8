import json
import re
import time
from datetime import datetime
import os


# this is the example "main" program
def request_data():
    # user input for time data
    while True:
        try:
            time_input = input("Enter a time in YYYY-MM-DD format: ")
            datetime.strptime(time_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid format. Please enter a time in YYYY-MM-DD format.")

    # user input for zipcode data
    while True:
        try:
            zipcode = input("Enter a 5 digit zipcode: ")

            if len(zipcode) == 5 and zipcode.isdigit():
                zipcode = int(zipcode)
                break
            else:
                print("Please try again.")
        except ValueError:
            print("Invalid format. Please enter a 5 digit zipcode.")

    # user input for temperature data
    while True:
        temperature = input("Enter optional temperature in XX.X format (or leave blank to pass): ")

        # check if the input is blank
        if temperature == "":
            temperature = None
            break

        # expression to match the XX.X format (two digits, a decimal point, and one digit)
        elif re.match(r'^\d{2}\.\d$', temperature):
            temperature = float(temperature)
            break
        else:
            print("Invalid format. Please enter a temperature in XX.X format, or leave blank.")

    # user input for humidity data
    while True:
        humidity = input("Enter optional humidity in WW.W format (or leave blank to pass): ")

        # check if the input is blank
        if humidity == "":
            humidity = None
            break

        # expression to match the WW.W format (two digits, a decimal point, and one digit)
        elif re.match(r'^\d{2}\.\d$', humidity):
            humidity = float(humidity)
            break
        else:
            print("Invalid format. Please enter a humidity in WW.W format, or leave blank.")

    # user input for precipitation data
    while True:
        precipitation = input("Enter optional precipitation in V.V format (or leave blank to pass): ")

        # check if the input is blank
        if precipitation == "":
            precipitation = None
            break

        # expression to match the V.V format (one digit, a decimal point, and one digit)
        elif re.match(r'^\d\.\d$', precipitation):
            precipitation = float(precipitation)
            break
        else:
            print("Invalid format. Please enter a precipitation in V.V format, or leave blank.")

    # create request dictionary with time and zipcode
    request = {
        'time': time_input,
        'zipcode': zipcode,
        'temperature': temperature,
        'humidity': humidity,
        'precipitation': precipitation
    }

    # write parameter data to request_data.json to be read by microservice
    with open('request_data.json', 'w') as f:
        json.dump(request, f)

    print("")
    print("Filtering parameters written to request_data.json:")
    print(request)
    print("")

    # wait for the microservice to process the request
    time.sleep(5)

    # read incoming filtered data from microservice
    while True:
        if os.path.exists('request_data.json'):
            with open('request_data.json', 'r') as f:
                data = json.load(f)
                break

    # display the response
    if data and data["filtered_results"]:
        print("Filtered dataset received:")
        for report in data["filtered_results"]:
            print(report)
    else:
        print("No data matches the given parameters. Please try again.")


if __name__ == "__main__":
    request_data()
