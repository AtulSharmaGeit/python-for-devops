import argparse
import json

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "UNKNOWN": 0}

    def read_logs(self):
        try:
            with open(self.log_file, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            print("Log file not found: ", self.log_file)
            return []
        
    def analyze(self, lines, level=None):
        for line in lines:
            if "INFO" in line:
                if not level or level == "INFO":
                    self.counts["INFO"] += 1
            elif "WARNING" in line:
                if not level or level == "WARNING":
                    self.counts["WARNING"] += 1
            elif "ERROR" in line:
                if not level or level == "ERROR":
                    self.counts["ERROR"] += 1
            else:
                if not level or level == "UNKNOWN":
                    self.counts["UNKNOWN"] += 1
        return self.counts
                
    def write_summary(self, out_file):
        print("Log Summary:")
        for level,count in self.counts.items():
            print(f"{level}: {count}")

        if out_file:
            with open(out_file, "w") as f:
                json.dump(self.counts, f, indent=4)
            print(f"Summary written to {out_file}")

def main():
    parser = argparse.ArgumentParser(description="Log Anayzer CLI")
    parser.add_argument("--file", required=True, help="Path to log file.")
    parser.add_argument("--out", required=True, help="Log Output to a file.")
    parser.add_argument("--level", help="Filter for level (Optional).")
    args = parser.parse_args()

    analyzer = LogAnalyzer(args.file)
    lines = analyzer.read_logs()

    if not lines:
        print("No logs to Analyze.")

    analyzer.analyze(lines, level=args.level)
    analyzer.write_summary(args.out)

if __name__ == "__main__":
    main()