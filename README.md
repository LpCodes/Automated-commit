# Automated Git Commit Script

A Python script that automatically commits and pushes changes to a Git repository, with a focus on logging and error handling.

## Features

- Automatically updates a log file with timestamps
- Commits and pushes changes to the specified Git branch
- Comprehensive error handling and logging
- Validates Git repository status
- Configurable repository path and branch
- Detailed logging to both file and console

## Requirements

- Python 3.6 or higher
- Git installed and configured on your system
- Git repository initialized in the target directory

## Installation

1. Clone this repository or download the script:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Make sure you have the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the script from the command line:
```bash
python app.py
```

### Configuration

The script can be configured by modifying the following parameters in the `GitAutoCommit` class:

- `repo_path`: Path to the Git repository (defaults to current directory)
- `branch`: Target branch for push operations (defaults to "main")

### Logging

The script creates two log files:
1. `git_auto_commit.log`: Contains detailed execution logs
2. `log.txt`: Contains timestamps of each commit

## How It Works

1. The script first validates that the current directory is a Git repository
2. Updates the `log.txt` file with the current timestamp
3. Checks for any changes in the repository
4. If changes are found:
   - Adds all changes to staging
   - Creates a commit with a timestamp-based message
   - Pushes changes to the specified branch
5. Logs all operations to both console and log file

## Error Handling

The script includes comprehensive error handling for:
- Invalid Git repository
- Failed Git commands
- File system errors
- Network issues during push

All errors are logged to both the console and the log file.

## Example Output

```
2024-03-21 10:30:45 - INFO - Log file updated successfully
2024-03-21 10:30:45 - INFO - Successfully committed and pushed changes
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
