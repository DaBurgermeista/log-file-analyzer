# Log File Analyzer

A simple Python tool to scan Linux-style authentication logs and summarize failed SSH login attempts

## How to Use

1. Add your `.log` file in the `logs/` folder
2. Run the script:

```bash
python3 analyzer.py
```

## Sample Output
```bash
192.168.1.10: 3 failed attempts
192.168.1.20: 1 failed attempts
```

## Future features
- Export to `CSV` or `JSON`
- Add visualization with `matplotlib`
- Visual charts (bar graphs for top IPs)
- Track timestamps of attacks
- Possible `Web UI` with `Flask`