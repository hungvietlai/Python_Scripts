"""
This script is designed to monitor the disk usage of a specified path on your computer and log a message indicating whether the disk usage exceeds a threshold percentage. 
If the used disk space percentage is above the threshold, it logs a warning; otherwise, it logs an informational message indicating that the disk usage is within acceptable limits.
The script can be customised via command-line arguments to check any path and threshold value.
If no arguments are provided, it defaults to checking the C:\ drive with a threshold of 40%.
"""

import shutil, logging, sys

log_file_path = 'path/to/log_file'

logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')

def check_disk_usage(path, threshold):
    try:
        total, used, _ = shutil.disk_usage(path)
        used_percentage = (used/total) * 100

        if used_percentage > threshold:
            return True, used_percentage
        else:
            return False, used_percentage
    except Exception as e:
        logging.error(f"Failed to check disk usage for {path}: {e}")
        return False, 0

if len(sys.argv) >= 3:
    path = sys.argv[1]
    threshold = int(sys.argv[2])
else:
    path = 'C:\\' # Default Path
    threshold = 40 # Default threshold

alert, usage = check_disk_usage(path, threshold)

if alert:
    logging.warning(f"ALERT: DISK usage for {path} is above {threshold}% : {usage:.2f}% used")
else:
    logging.info(f"Disk usage for {path} is below {threshold}% : {usage:.2f}% used")




