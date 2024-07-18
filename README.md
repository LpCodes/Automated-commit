
# Setting Up a Cron Job to Run Every 5 Minutes

To create a cron job that runs every 5 minutes and executes your Python script, follow these steps:

## 1. Save the Python Script

Save the Python script you provided into a file, for example `daily_commit.py`.

## 2. Make the Script Executable (Optional but Recommended)

Change the file permissions to make the script executable.

``` bash
chmod +x /path/to/daily_commit.py
```

## 3. Edit the Crontab File

Open your crontab file for editing by running the following command in your terminal:

```bash
crontab -e
```

## 4. Add the Cron Job

Add the following line to the crontab file to run the script every 5 minutes.

```plaintext
*/5 * * * * /usr/bin/python3 /path/to/daily_commit.py
```

Make sure to replace `/usr/bin/python3` with the path to your Python interpreter if it's different, and `/path/to/daily_commit.py` with the actual path to your script.
