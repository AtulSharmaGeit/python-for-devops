import json

class LogAnalyzer:
    def __init__(self, log_file, output_file="log_summmary.json"):
        self.log_file = log_file
        self.output_file = output_file
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "UNKNOWN": 0}

    def read_logs(self):
        try:
            with open(self.log_file, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            print("Log file not found: ", self.log_file)
            return []

    def analyze(self, lines):
        for line in lines:
            if "INFO" in line:
                self.counts["INFO"] += 1
            elif "WARNING" in line:
                self.counts["WARNING"] += 1
            elif "ERROR" in line:
                self.counts["ERROR"] += 1
            else:
                self.counts["UNKNOWN"] += 1
        return self.counts
        
    def write_summary(self):
        print("Log Analysis Summary:")
        for level,count in self.counts.items():
            print(f"{level}: {count}")

        with open(self.output_file, "w") as file:
            json.dump(self.counts, file)

        print(f"\n Summary Written in {self.output_file}")

def main():
    analyzer = LogAnalyzer("app.log")

    lines = analyzer.read_logs()

    if not lines:
        print("No logs to analyze.")
        return

    analyzer.analyze(lines)
    analyzer.write_summary()

if __name__ == "__main__":
    main()