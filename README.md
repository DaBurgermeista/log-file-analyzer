# 🕵️‍♂️ Log File Analyzer

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/DaBurgermeista/log-file-analyzer?style=flat-square)
![Issues](https://img.shields.io/github/issues/DaBurgermeista/log-file-analyzer?style=flat-square)
![Pull Requests](https://img.shields.io/github/issues-pr/DaBurgermeista/log-file-analyzer?style=flat-square)
![Built with ❤️](https://img.shields.io/badge/Built%20with-%E2%9D%A4-red?style=flat-square)


A simple Python tool to scan Linux-style authentication logs and summarize failed SSH login attempts by IP address.

---

## 🚀 Features

- ✅ Parses `auth.log` or similar files
- ✅ Counts failed login attempts by IP
- ✅ Exports results to CSV
- ✅ Visualizes attempts with a bar chart
- 🔜 Planned: JSON export, timestamp analysis, real-time alerts

---

## 📂 Sample Log Format

```bash
Jun 20 10:01:23 server sshd[12345]: Failed password for invalid user testuser from 192.168.1.10 port 54321 ssh2
```
---
## How to Use

1. Clone the repo and install dependencies

```bash
pip install -r requirements.txt
```
2. Run the analyzer
```bash
python3 analyzer.py
```
3. Export the results to CSV:
```bash
python3 analyzer.py --export
```
4. Visualize failed logins as a bar chart
```bash
python3 analyzer.py --plot
```
The plot will be saved as `failed_logins_char.png` and displayed in a pop-up
---
## Example Output Chart
![alt text](docs/failed_logins_chart.png)

---

## Requirements
- Python 3.9+
- pandas
- matplotlib

---

## Contributions
Feel free to fork and suggest features like:
- Brute force detection
- IP geolocation
- Real-time monitoring

## Author
Built with ❤️ by DaBurgermeista
Inspired by real-world blue team needs.