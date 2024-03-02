"""
This Python script is designed to automate the process of ensuring all .conf files within a specific directory (/etc/myapp/configs/) have their logging level set to DEBUG.
The script is designed to update the log_level setting if it exists, or appending it if not. 
The script incorporates Python's logging module, directing informational messages about file updates and error messages to a designated log file (/path/to/log_file). 

"""

import os, re, logging

logging.basicConfig(filename='/path/to/log_file', level=logging.INFO, 
                    format='%(asctime)s-%(levelname)s-%(message)s')

path = ('/etc/myapp/configs/')
config_pattern = re.compile(r'.*\.conf$')
log_level_pattern = re.compile(r'^(log_level=)(.*?)$', re.MULTILINE)

for root, _, f_names in os.walk(path):
    for f in f_names:
        if config_pattern.match(f):
            file_path = os.path.join(root, f)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                new_content, num_replacemnts = log_level_pattern.subn(r'\1DEBUG', content)

                if num_replacemnts == 0:
                    new_content += '\nlog_level=DEBUG\n'
                    
                with open(file_path, 'w') as f:
                    f.write(new_content)

                logging.info(f"Updated {file_path}")

            except Exception as e:
                logging.error(f"Error Updating {file_path}: {e}")

