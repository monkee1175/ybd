import os
import signal
import time
import subprocess


# @S4 OFFICIAL GRP# Set the path to the script you want to restart
script_to_restart = "new.py"

def restart_script():
    # @S4 OFFICIAL GRP# Run the script
    print("LOOP START BY YBD.....")
    process = subprocess.Popen(["python3", script_to_restart], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    process = restart_script()
    while True:
        time.sleep(480)  # @S4 OFFICIAL GRP # Sleep for 30 seconds
        # @S4 OFFICIAL GRP # Send Ctrl+C signal to the process
        process.send_signal(signal.SIGINT)
        # @S4 OFFICIAL GRP # Wait for the process to terminate
        process.wait()
        # @S4 OFFICIAL GRP # Restart the script
        process = restart_script()

if __name__ == "__main__":
    main()