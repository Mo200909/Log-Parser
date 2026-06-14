# Log Parser

A simple Python utility that extracts IP addresses from server log files and generates a frequency report in CSV format.

---

## What It Does

The script reads an HTTP server log file, finds all IP addresses using regex pattern matching, counts how many times each IP appears, and exports the results to a CSV file for easy analysis.

**Input:** Apache/Nginx server log file
**Output:** CSV file with IP addresses and their access frequency

---

## Files

- **Log_parser.py** — Main Python script
- **log.txt** — Sample server log file (Apache format)
- **output.csv** — Generated report with IP frequencies

---

## How It Works

**Three main functions:**

1. `reader(filename)` — Opens the log file and extracts all IP addresses using regex pattern `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}` (matches standard IPv4 format)

2. `count(ips_list)` — Uses Python's `Counter` from collections to tally how many times each IP appears

3. `write_csv(counter)` — Writes results to `output.csv` with two columns: IP address and access frequency

---

## Usage

```bash
python Log_parser.py
```

This processes `log.txt` and creates `output.csv` in the same directory.

---

## Sample Output

| IP | Frequency |
|---|---|
| 194.6.231.248 | 22 |
| 185.26.180.145 | 21 |
| 93.72.5.44 | 20 |
| 93.84.16.70 | 13 |
| 66.249.81.205 | 8 |
| 66.249.81.211 | 8 |

---

## Use Cases

- **Security analysis** — Identify which IPs are accessing your server most frequently
- **Traffic monitoring** — Spot bot activity or suspicious access patterns
- **Performance optimization** — Determine which clients consume the most bandwidth
- **Threat investigation** — Investigate suspicious IP sources in access logs

---

## Technologies

- **Python 3** — Core language
- **re module** — Regular expression pattern matching for IP extraction
- **collections.Counter** — Efficient frequency counting
- **csv module** — CSV file output

---

## Author

Mofolorunsho Adeleke
