import json
import time
import os


# small sample log data for testing
log = [
    {'time': '2025-02-16', 'zipcode': 10001, 'temperature': 50.0, 'humidity': 60.0, 'precipitation': 0.1},
    {'time': '2025-02-16', 'zipcode': 10001, 'temperature': 55.5, 'humidity': 65.5, 'precipitation': 0.2},
    {'time': '2025-02-16', 'zipcode': 20001, 'temperature': 48.7, 'humidity': 70.7, 'precipitation': 0.3},
    {'time': '2025-02-16', 'zipcode': 10001, 'temperature': 45.8, 'humidity': 50.8, 'precipitation': 0.0}
]


# this is Microservice A
def process_request():

    print("Listening...\n")

    if os.path.exists('request_data.json'):
        current_mod_time = os.path.getmtime('request_data.json')
    else:
        current_mod_time = 0

    while True:
        if os.path.exists('request_data.json'):
            new_mod_time = os.path.getmtime('request_data.json')

            if new_mod_time != current_mod_time:
                current_mod_time = new_mod_time

                with open('request_data.json', 'r') as f:
                    try:
                        request = json.load(f)
                    except json.JSONDecodeError:
                        print("Invalid JSON format, request not processed.")
                        continue

                # check if the request was already processed
                if request.get("processed"):
                    continue

                output_list = []

                # iterate over log data and find matching data
                for report in log:
                    if request['time'] == report['time'] and request['zipcode'] == report['zipcode']:
                        if (request['temperature'] is None or request['temperature'] == report['temperature']) and \
                           (request['humidity'] is None or request['humidity'] == report['humidity']) and \
                           (request['precipitation'] is None or request['precipitation'] == report['precipitation']):
                            output_list.append(report)

                if request.get("processed") is None:
                    print("Filtering parameters received by request_data.json:")
                    print(request)
                    print("")

                # add "processed" flag and write back to the same file
                request["filtered_results"] = output_list
                request["processed"] = True

                # write result to response_data.json to be read by main program
                with open('request_data.json', 'w') as f:
                    json.dump(request, f, indent=2)

                print("Filtered data has been written to request_data.json:")
                for report in output_list:
                    print(report)

                print("")
                print("Listening...")

        # wait a bit
        time.sleep(2)


if __name__ == "__main__":
    process_request()
