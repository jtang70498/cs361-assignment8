import json
import re
from datetime import datetime


# this is Microservice A
def request_data(log=None):
    # check if log data exists
    if log is None:
        raise ValueError("Please provide log data")

    # user input for time data
    while True:
        try:
            time = input("Enter a time in YYYY-MM-DD format: ")
            datetime.strptime(time, "%Y-%m-%d")
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
        'time': time,
        'zipcode': zipcode,
        'temperature': temperature,
        'humidity': humidity,
        'precipitation': precipitation
    }

    output_list = []

    for report in log:
        # check if time and zipcode match
        if request['time'] == report['time'] and request['zipcode'] == report['zipcode']:
            # check if optional condition (temperature, humidity, precipitation) is provided
            if (request['temperature'] is None or request['temperature'] == report['temperature']) and \
                    (request['humidity'] is None or request['humidity'] == report['humidity']) and \
                    (request['precipitation'] is None or request['precipitation'] == report['precipitation']):
                output_list.append(report)

    # write result to a response_data.json to be read by response.py
    with open('response_data.json', 'w') as f:
        json.dump(output_list, f)
    print(f"Data has been written to response_data.json: {request}")


# small sample log data for testing
log_data = [
    {'time': '2025-02-16', 'zipcode': 10001, 'temperature': 50.0, 'humidity': 60.0, 'precipitation': 0.1},
    {'time': '2025-02-16', 'zipcode': 10001, 'temperature': 55.5, 'humidity': 65.5, 'precipitation': 0.2},
    {'time': '2025-02-16', 'zipcode': 20001, 'temperature': 48.7, 'humidity': 70.7, 'precipitation': 0.3},
    {'time': '2025-02-16', 'zipcode': 10001, 'temperature': 45.8, 'humidity': 50.8, 'precipitation': 0.0}
]
request_data(log=log_data)
