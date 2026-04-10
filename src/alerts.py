def generate_alerts(data):
    print("\n🚨 ALERTS:")

    alert_found = False

    for ip, row in data.iterrows():
        if row['anomaly'] == -1:
            alert_found = True
            print(f"⚠️ Suspicious activity detected from IP: {ip}")
            print(f"   ➤ Login attempts: {row['attempt']}")
            print("   ➤ Possible brute-force attack\n")

    if not alert_found:
        print("✅ No suspicious activity detected")