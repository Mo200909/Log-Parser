# Log Parser & Anomaly Detector

A Python utility that extracts IP addresses from server log files, generates a frequency report, and automatically detects anomalous traffic patterns.

---

## What It Does

The script reads an HTTP server log file, finds all IP addresses using regex pattern matching, and counts how many times each IP appears. It exports the standard results to a CSV file and immediately scans that data to flag any IP addresses exceeding a normal traffic threshold (e.g., potential DDoS attacks, aggressive scraping, or brute-force attempts). Suspicious IPs are isolated and exported to a dedicated anomaly report.

**Input:** Apache/Nginx server log file
**Outputs:** 1. `output.csv` — Full report with all IP addresses and their access frequencies.
2. `anomaly_report.csv` — Isolated report of IPs exceeding the safe request threshold.

---

## Files

- **Log_parser.py** — Main Python script
- **log.txt** / **log(anomaly).txt** — Sample server log files
- **output.csv** — Generated standard report
- **anomaly_report.csv** — Generated anomaly report

---

## How It Works

[Image of basic log analysis workflow]

**Four main functions:**

1. `reader(filename)` — Opens the log file and extracts all IP addresses using the regex pattern `\b(?:\d{1,3}\.){3}\d{1,3}\b` (matches standard IPv4 format using strict word boundaries).
2. `count(ips_list)` — Uses Python's `Counter` from the `collections` module to tally how many times each IP appears.
3. `write_csv(counter)` — Writes standard baseline results to `output.csv` with two columns: IP address and access frequency.
4. `analyze_traffic(input_csv, anomaly_threshold)` — Scans `output.csv` against a defined traffic threshold (default is 20). If an IP exceeds this limit, the script triggers a console alert and writes the offender to `anomaly_report.csv`.

---

## Usage

```bash
python Log_parser.py
```

This processes the configured log file, prints console alerts if threats are found, and creates the required CSV files in the same directory.

---

## Sample Output

### Standard Output (`output.csv`)

| IP | Frequency |
|---|---|
| 194.6.231.248 | 22 |
| 185.26.180.145 | 21 |
| 93.72.5.44 | 20 |
| 93.84.16.70 | 13 |
| 66.249.81.205 | 8 |

### Console Alert & `anomaly_report.csv`

```text
 ANOMALIES DETECTED 
-------------------------
Suspicious IP: 194.6.231.248 | Frequency: 22
Suspicious IP: 185.26.180.145 | Frequency: 21

Anomaly report saved to 'anomaly_report.csv'.
```

| Anomalous IP | Frequency |
|---|---|
| 194.6.231.248 | 22 |
| 185.26.180.145 | 21 |

---

## Use Cases

- **Automated Threat Detection** — Automatically isolate DDoS-like traffic spikes or brute-force attempts.
- **Security analysis** — Identify which IPs are accessing your server most frequently.
- **Traffic monitoring** — Spot bot activity, web scrapers, or suspicious access patterns.
- **Performance optimization** — Determine which clients consume the most bandwidth.

---

## Technologies

- **Python 3** — Core language
- **re module** — Regular expression pattern matching for accurate IP extraction
- **collections.Counter** — Efficient frequency counting
- **csv module** — Handling both the reading and writing of report files

---

## Author

Mofolorunsho Adeleke
