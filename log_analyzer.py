def detect_suspicious_logs(log_text):
    alerts = []

    suspicious_keywords = [
        "failed login",
        "unauthorized",
        "error",
        "denied",
        "attack",
        "malware"
    ]

    lines = log_text.split("\n")

    for line in lines:
        for keyword in suspicious_keywords:
            if keyword.lower() in line.lower():
                alerts.append(line)
                break

    return alerts
