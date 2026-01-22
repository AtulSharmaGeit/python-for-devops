# THINKING BEFORE CODING!!!
Today, I took one of my earlier scripts (log_analyzer_cli.py) and documented it.

The focus was on design thinking – pausing before writing automation code and asking the right questions.

## What problem am I solving?
- I want to analyze server log files quickly.

- Manually searching logs is slow and error-prone.

- My script should help DevOps engineers find useful info (like errors, warnings, counts) in seconds.

## What input does my script need?
- A log file path (example: `app.log`)

- Optional arguments (like `--error`, `--warning`, `--count`) from the user via CLI

## What output should my script give?
- Filtered log lines (errors/warnings)

- Summary counts (e.g., how many errors/warnings)

- Clear, readable text output in the terminal

## What are the main steps?
- Step 1: Take input file path from user

- Step 2: Open and read the log file safely

- Step 3: Apply filters (error/warning) based on user’s choice

- Step 4: Count occurrences if requested

- Step 5: Print results in a clean format