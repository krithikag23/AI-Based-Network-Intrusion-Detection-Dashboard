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
