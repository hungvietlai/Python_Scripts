"""
This script navigates the '/var/log/' directory to identify and count occurrences of 'ERROR' within each log file. 
It generates a summary in 'error_summary.txt'.
"""

import os, re
path =('/var/log/')
pattern = re.compile(r'\bERROR\b')
summary_path = ('path/to/error_summary.txt')

for root, _, f_names in os.walk(path):
    for f in f_names:
        file_path = os.path.join(root, f)
        local_count = 0 
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if pattern.search(line):
                        local_count += 1
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
        
        if local_count > 0:
            try:
                with open(summary_path, 'a') as summary_file:
                    summary_file.write(f"{file_path}: {local_count} ERROR(s)\n")
                    print(f"{file_path}: {local_count} ERROR(s)")
            except Exception as e:
                print(f"Error writing to {summary_path}: {e}")




     
