# Firewall Log Analyzer
# Author: ACL
# Description: Analyzes firewall logs to count allowed and blocked actions.
# Date: 2025

import re

# Function to read and parse firewall logs (ACL)
def parse_log(file_path):
    allowed = 0
    blocked = 0

    with open(file_path, 'r') as file:
        logs = file.readlines()
    
    for log in logs:
        # Extract action (ALLOW or BLOCK) using regex
        match = re.search(r'ACTION=(\w+)', log)
        if match:
            action = match.group(1)
            if action == "ALLOW":
                allowed += 1
            elif action == "BLOCK":
                blocked += 1

    return allowed, blocked

# Main function to run the script (ACL)
def main():
    file_path = 'firewall_logs.txt'  # Path to the log file
    allowed, blocked = parse_log(file_path)

    # Output the results
    print(f"Logs analysis completed for: {file_path}")
    print(f"Total Allowed connections: {allowed}")
    print(f"Total Blocked connections: {blocked}")

if __name__ == "__main__":
    main()
