import re
from collections import Counter
import csv

#Finds IP addresses on lists
def reader(filename):
    with open(filename) as f:
        log = f.read()
        print(log)

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

        ips_list = re.findall(regexp, log)

        return (ips_list)

def count(ips_list):
    return Counter(ips_list)

#writes CSV file for IP addresses

def write_csv(counter):
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP', 'Frequency']
        writer.writerow(header)

        for item in counter:
            writer.writerow([item, counter[item]])

if   __name__ == '__main__':
    write_csv(count(reader('log.txt')))
