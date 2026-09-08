def analyze_logs(file_path):
    print("--- Starting Log Analysis ---\n")
    alerts_found = 0

    with open(file_path, 'r') as file:
        for line in file:
            if "WARNING" in line or "Failed password" in line:
                print(f"[ALERT DETECTED]: {line.strip()}")
                alerts_found += 1

    print(f"\n--- Analysis Complete: Found {alerts_found} potential security issues. ---")

if __name__ == "__main__":
    analyze_logs("sample_logs.log")