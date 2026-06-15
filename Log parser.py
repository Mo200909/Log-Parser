import re
from collections import Counter
import csv


# Finds IP addresses on lists
def reader(filename):
    with open(filename) as f:
        log = f.read()
        print(log)

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

        ips_list = re.findall(regexp, log)

        return ips_list


def count(ips_list):
    return Counter(ips_list)


# writes CSV file for IP addresses
def write_csv(counter):
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP', 'Frequency']
        writer.writerow(header)

        for item in counter:
            writer.writerow([item, counter[item]])


def analyze_traffic(input_csv="output.csv", anomaly_threshold=20):
    anomalous_ips = {}

    try:
        with open(input_csv, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                if len(row) == 2:
                    ip = row[0]
                    frequency = int(row[1])

                    if frequency > anomaly_threshold:
                        anomalous_ips[ip] = frequency

    except FileNotFoundError:
        print(f"Error: File {input_csv} not found.")
        return

    # Print and save results
    if anomalous_ips:
        print('\n Anomaly Detected')
        print("-" * 25)

        # 1. Print the issues to the screen
        for ip, freq in anomalous_ips.items():
            print(f"Suspicious IP: {ip} | Frequency: {freq}")

        # 2. Save the issues to the file
        report_file = 'anomaly_report.csv'
        with open(report_file, 'w', newline='') as report:
            writer = csv.writer(report)
            writer.writerow(['Anomalous IP', 'Frequency'])  # Added a header row for cleanliness
            for ip, freq in anomalous_ips.items():
                writer.writerow([ip, freq])

        print(f"\nAnomaly report saved to '{report_file}'.")
    else:
        print("\n No anomalies detected. Traffic is within normal limits.")


if __name__ == '__main__':
    write_csv(count(reader('log(anomaly).txt')))
    analyze_traffic('output.csv', anomaly_threshold=20)
