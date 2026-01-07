import json
def read_log():
    try:
        with open("app.log", "r") as log_file:
            lines = log_file.readlines()
            return lines
            
    except FileNotFoundError:
        print("Error: app.log file is not found.")

def analyze_log(lines):

    counts = {
        "INFO":0,
        "WARNING":0,
        "ERROR":0
    }
         
    for line in lines:
        if "INFO" in line:
            counts["INFO"] += 1
        elif "WARNING" in line:
            counts["WARNING"] += 1
        elif "ERROR" in line:
            counts["ERROR"] +=1
        else:
            pass

    print("Log Summary:")
    print("INFO: ", counts["INFO"])
    print("WARNING: ", counts["WARNING"])
    print("ERROR: ", counts["ERROR"])

    with open("log_summary.json", "w") as output_file:
       json.dump(counts, output_file)

    print("\nSummary written to log_summary.json")

lines = read_log()
analyze_log(lines)