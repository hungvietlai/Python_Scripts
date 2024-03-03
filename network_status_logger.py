"""
This script is a network status checker designed to verify the accessibility of a specified URL by performing an HTTP GET request.
It uses the requests library to make the request and then logs the outcome using Python's logging module.
If the URL is successfully reached, an informational log entry is recorded, noting the URL and its reachable status.
For any other status code, a warning is logged, indicating the URL is not reachable along with the received status code. 
In case of an exception, an error is logged with the details of the failure.
"""

import requests, logging

logging.basicConfig(filename='/path/to/log_file', level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')

def check_network_status(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            logging.info(f"{url} is reachable, status_code: {response.status_code}")
        else:
            logging.warning(f"{url} is not reachable, status_code: {response.status_code}")
    except Exception as e:
        logging.error(f"Failed to reach {url}: {e}")

url = "https://www.google.com"
check_network_status(url)