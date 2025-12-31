Log Analyzer Tool
=================

This Python script analyzes error logs, summarizes errors and warnings, and provides a clear report.

Features:
- Reads any log file following the format: `timestamp LEVEL message` (e.g., `2025-12-30 10:12:01 ERROR FileNotFoundError: File 'data.csv' not found`).
- Counts and groups repeated ERROR and WARNING messages.
- Displays total lines processed.
- Handles missing log files gracefully.
- Uses argparse for command-line input.

Requirements:
- Python 3.x

Usage:
1. Save your log file (e.g., `error.log`).
2. Save the script as `log_analyzer.py`.
3. Run the script from the terminal:

```bash
python log_analyzer.py error.log
```

Output Example:
```
Total lines processed: 4

---- ERROR SUMMARY ----
2x : FileNotFoundError: File 'data.csv' not found
1x : KeyError: 'username'
1x : FileNotFoundError: File 'config.json' not found

---- WARNING SUMMARY ----
1x : Low disk space
```

Enhancements:
- Can be extended to save summaries to CSV or JSON.
- Can filter logs by date range.
- Can sort errors by frequency.

Author:
- Your Name

License:
- MIT License

