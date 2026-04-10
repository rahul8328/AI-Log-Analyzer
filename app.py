from flask import Flask, render_template
from main import run_analysis

app = Flask(__name__)

@app.route("/")
def home():
    logs_df, result_df, suspicious_ips, normal_ips = run_analysis()

    total_logs = len(logs_df)
    total_ips = len(result_df)
    suspicious_count = len(suspicious_ips)
    normal_count = len(normal_ips)

    return render_template(
        "index.html",
        logs=logs_df.to_dict(orient="records"),
        results=result_df.reset_index().to_dict(orient="records"),
        suspicious=suspicious_ips.reset_index().to_dict(orient="records"),
        total_logs=total_logs,
        total_ips=total_ips,
        suspicious_count=suspicious_count,
        normal_count=normal_count
    )

if __name__ == "__main__":
    app.run(debug=True)