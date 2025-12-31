import re
from collections import Counter
import argparse
import os

# -----------------------------
# Function to parse log lines
# -----------------------------
def parse_log_line(line):
    """
    Parse a log line and extract timestamp, log level, and message.
    Example line:
    2025-12-30 10:12:01 ERROR FileNotFoundError: File 'data.csv' not found
    """
    pattern = r"^(?P<timestamp>\S+ \S+)\s+(?P<level>\S+)\s+(?P<message>.+)$"
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return None

# -----------------------------
# Function to analyze log file
# -----------------------------
def analyze_log(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    error_counter = Counter()
    warning_counter = Counter()
    total_lines = 0

    with open(file_path, "r") as f:
        for line in f:
            total_lines += 1
            parsed = parse_log_line(line.strip())
            if parsed:
                level = parsed["level"]
                message = parsed["message"]
                if level == "ERROR":
                    error_counter[message] += 1
                elif level == "WARNING":
                    warning_counter[message] += 1

    # -----------------------------
    # Display results
    # -----------------------------
    print(f"\nTotal lines processed: {total_lines}\n")
    
    if error_counter:
        print("---- ERROR SUMMARY ----")
        for msg, count in error_counter.most_common():
            print(f"{count}x : {msg}")
    
    if warning_counter:
        print("\n---- WARNING SUMMARY ----")
        for msg, count in warning_counter.most_common():
            print(f"{count}x : {msg}")

# -----------------------------
# Main entry point with argparse
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Log Analyzer Tool")
    parser.add_argument(
        "logfile", type=str, help="Path to the log file to analyze"
    )
    args = parser.parse_args()
    analyze_log(args.logfile)

if __name__ == "__main__":
    main()
