import re
import pandas as pd

def parse_logs(file_path):
    data = []

    pattern = re.compile(
        r'^(?P<month>\w{3})\s+'
        r'(?P<day>\d{1,2})\s+'
        r'(?P<time>\d{2}:\d{2}:\d{2})\s+'
        r'(?P<host>\S+)\s+'
        r'(?P<service>\S+):\s+'
        r'(?P<message>.*)$'
    )

    ip_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            match = pattern.match(line)
            if not match:
                continue

            message = match.group("message")
            ip_match = ip_pattern.search(message)
            ip = ip_match.group(1) if ip_match else "N/A"

            if "Failed password" in message:
                status = "failed"
            elif "Accepted password" in message:
                status = "success"
            else:
                status = "unknown"

            data.append({
                "month": match.group("month"),
                "day": match.group("day"),
                "time": match.group("time"),
                "host": match.group("host"),
                "service": match.group("service"),
                "log_name": match.group("service").split("[")[0],
                "message": message,
                "ip": ip,
                "status": status
            })

    return pd.DataFrame(data)