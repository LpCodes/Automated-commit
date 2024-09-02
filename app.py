import subprocess
from datetime import datetime
import os


repo_path = os.getcwd()


file_path = os.path.join(repo_path, "log.txt")


now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")


with open(file_path, "a") as file:
    file.write(current_time + "\n")


def run_git_command(command):
    result = subprocess.run(command, cwd=repo_path, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout


run_git_command("git add .")


commit_message = f"Auto-commit: updated log.txt on {current_time}"
run_git_command(f'git commit -m "{commit_message}"')


run_git_command("git push origin main")  
