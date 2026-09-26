# IP Traffic Anomaly Detector

Parses IP addresses from a log file, counts frequency, and flags IPs above a threshold as anomalous.

## What it does

1. **Reads log file** — extracts all IPv4 addresses via regex from a text log.
2. **Counts occurrences** — tallies frequency per IP using `collections.Counter`.
3. **Writes CSV** — outputs `output.csv` with columns `IP, Frequency`.
4. **Flags anomalies** — any IP exceeding `anomaly_threshold` (default 20) is printed and saved to `anomaly_report.csv`.

## Usage

```bash
python script.py
```

Requires a file named `log(anomaly).txt` in the same directory (hardcoded in `__main__`).

## Output files

| File | Contents |
|---|---|
| `output.csv` | Every unique IP found, with hit count |
| `anomaly_report.csv` | Only IPs above threshold (created only if anomalies exist) |

## Config

- `anomaly_threshold` (default `20`) — change in the `analyze_traffic()` call.
- Input filename is hardcoded (`log(anomaly).txt`) — no CLI args.

## Known gaps

- Regex matches any 4-dot-separated number pattern, including invalid IPs (e.g. `999.999.999.999`) — no validation.
- `reader()` prints the entire log to stdout — noisy for large files, no way to suppress.
- Input filename hardcoded, not parameterized via CLI/argparse.
- No logging/timestamp on anomaly detections — just raw frequency count, no time-window analysis (a burst over 1 min vs spread over a week look identical).
