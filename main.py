from src.parser import parse_logs
from src.model import detect_anomalies

def run_analysis():
    log_file = "logs/auth.log"
    logs_df = parse_logs(log_file)

    logs_df["attempt"] = 1

    features = logs_df.groupby("ip")["attempt"].sum().to_frame()
    result_df = detect_anomalies(features)

    suspicious_ips = result_df[result_df["anomaly"] == -1].copy()
    normal_ips = result_df[result_df["anomaly"] == 1].copy()

    return logs_df, result_df, suspicious_ips, normal_ips