import os
import subprocess
from datetime import datetime

# Get the current working directory
repo_path = os.getcwd()
file_path = os.path.join(repo_path, 'daily_commit.txt')

# Write current date and time to the file
with open(file_path, 'a') as f:
    f.write(f'Commit made on {datetime.now()}\n')

# Change to the repository directory
os.chdir(repo_path)

# Add the file to the staging area
subprocess.run(['git', 'add', file_path], check=True)

# Commit the changes
subprocess.run(['git', 'commit', '-m', 'Automated daily commit'], check=True)

# Push the changes
subprocess.run(['git', 'push'], check=True)
