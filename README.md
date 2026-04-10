# 🔐 AI-Based Log Analysis & Threat Detection System

## 📌 Overview
This project is a **SOC (Security Operations Center) style log analysis system** that uses **Machine Learning (AI)** to detect suspicious activities such as brute-force attacks from system logs.

It simulates how modern SIEM tools analyze logs, detect anomalies, and generate alerts.

---

## 🚀 Features

- 📄 Log Parsing (SSH/System logs)
- 🧠 AI-Based Anomaly Detection (Isolation Forest)
- 🚨 Alert Generation for suspicious IPs
- 🌐 Web Dashboard (Flask)
- 📊 Log Visualization with status (Success/Failed)
- 🕒 Displays timestamp, log name, and message
- 📡 Identifies brute-force attack patterns

---

## 🏗️ Project Structure


AI-Log-Analyzer/
│
├── logs/
├── src/
├── templates/
├── static/
├── app.py
├── main.py
├── requirements.txt
└── README.md


---

## ⚙️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Flask
- HTML, CSS

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py

Then open:

http://127.0.0.1:5000/
🎯 Use Case
SOC Monitoring
Brute-force Detection
Log Analysis Automation

👨‍💻 Author

Rahul Gollapelly