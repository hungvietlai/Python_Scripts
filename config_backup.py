"""
This Python script is designed to back up .conf configuration files from a specified directory ('/etc/myapp/configs/') to a backup directory ('path/to/config_backup/').
It scans all subdirectories within the base path for files matching the .conf extension. 
For each configuration file found, the script checks if it has been modified within the last day compared to the last backup timestamp.
It is then copied to the backup directory, preserving the original directory structure. 
"""


import os, re, datetime, shutil

def file_needs_backup(source_file, last_backup_time):
    file_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(source_file))
    return file_mod_time > last_backup_time

base_path = ('/etc/myapp/configs/')
backup_dir = ('path/to/config_backup/')
config_pattern = re.compile('.*\.conf$')

last_backup_time = datetime.datetime.now() - datetime.timedelta(days=1)

if not os.path.exists(backup_dir):
    os.makedirs(backup_dir, exist_ok=True)

for root, _, f_names in os.walk(base_path):
    for f in f_names:
        if config_pattern.match(f):
            file_path = os.path.join(root, f)
            if file_needs_backup(file_path, last_backup_time):
                    rel_path = os.path.relpath(file_path, start=base_path)
                    backup_file_path = os.path.join(backup_dir, rel_path)
                    os.makedirs(os.path.dirname(backup_file_path), exist_ok=True)
                    shutil.copy2(file_path, backup_file_path)
                    print(f"Copied {file_path} to {backup_file_path}")





