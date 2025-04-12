import subprocess
import logging
from datetime import datetime
import os
import sys
from typing import Optional, Tuple


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('git_auto_commit.log'),
        logging.StreamHandler(sys.stdout)
    ]
)


class GitAutoCommit:
    def __init__(self, repo_path: str = None, branch: str = "main"):
        """
        Initialize GitAutoCommit with repository path and target branch.
        
        Args:
            repo_path (str, optional): Path to the Git repository. Defaults to current directory.
            branch (str, optional): Target branch for push. Defaults to "main".
        """
        self.repo_path = repo_path or os.getcwd()
        self.branch = branch
        self.log_file = os.path.join(self.repo_path, "log.txt")
        
        if not self._is_git_repo():
            raise ValueError(f"'{self.repo_path}' is not a valid Git repository")

    def _is_git_repo(self) -> bool:
        """Check if the directory is a Git repository."""
        return self._run_git_command("git rev-parse --is-inside-work-tree")[0]

    def _run_git_command(self, command: str) -> Tuple[bool, str]:
        """
        Run a Git command and return success status and output.
        
        Args:
            command (str): Git command to execute
            
        Returns:
            Tuple[bool, str]: Success status and command output/error
        """
        try:
            result = subprocess.run(
                command,
                cwd=self.repo_path,
                shell=True,
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                logging.error(f"Git command failed: {result.stderr}")
                return False, result.stderr
            return True, result.stdout.strip()
        except Exception as e:
            logging.error(f"Error executing git command: {str(e)}")
            return False, str(e)

    def update_log_file(self) -> bool:
        """Update the log file with current timestamp."""
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_file, "a") as file:
                file.write(current_time + "\n")
            logging.info("Log file updated successfully")
            return True
        except Exception as e:
            logging.error(f"Failed to update log file: {str(e)}")
            return False

    def has_changes(self) -> bool:
        """Check if there are any changes to commit."""
        success, output = self._run_git_command("git status --porcelain")
        return success and bool(output)

    def commit_and_push(self) -> bool:
        """Perform the commit and push operation."""
        if not self.has_changes():
            logging.info("No changes to commit")
            return True

        # Add changes
        success, output = self._run_git_command("git add .")
        if not success:
            return False

        # Create commit
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Auto-commit: updated log.txt on {current_time}"
        success, output = self._run_git_command(f'git commit -m "{commit_message}"')
        if not success:
            return False

        # Push changes
        success, output = self._run_git_command(f"git push origin {self.branch}")
        if not success:
            return False

        logging.info("Successfully committed and pushed changes")
        return True


def main():
    """Main function to run the auto-commit process."""
    try:
        auto_commit = GitAutoCommit()
        
        if not auto_commit.update_log_file():
            sys.exit(1)
            
        if not auto_commit.commit_and_push():
            sys.exit(1)
            
    except Exception as e:
        logging.error(f"Script failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()  