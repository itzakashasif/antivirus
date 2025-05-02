# antivirus
Open it on your terminal
import os
import logging

# Configure logging
logging.basicConfig(
    filename="scan_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Sample virus signatures (for educational use)
VIRUS_SIGNATURES = [
    "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
]

def scan_file(file_path):
    try:
        with open(file_path, 'r', errors='ignore') as file:
            content = file.read()
            for signature in VIRUS_SIGNATURES:
                if signature in content:
                    return True
    except Exception as e:
        logging.warning(f"Failed to read {file_path}: {e}")
    return False

def scan_directory(directory):
    print(f"\nStarting scan in: {directory}\n")
    infected = []

    for root, _, files in os.walk(directory):
        for name in files:
            if name.endswith(('.txt', '.py', '.exe')):
                file_path = os.path.join(root, name)
                if scan_file(file_path):
                    infected.append(file_path)
                    logging.info(f"Infected: {file_path}")

    if infected:
        print("Infected files detected:\n")
        for file in infected:
            print(f" - {file}")
    else:
        print("No infections found.")

    print("\nScan complete. Log saved to 'scan_log.txt'.")

if __name__ == "__main__":
    path = input("Enter the directory path to scan: ").strip()
    if os.path.isdir(path):
        scan_directory(path)
    else:
        print("Invalid directory path!")
