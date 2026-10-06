"""Small defensive SOC triage engine for the ARYA portfolio demo."""


def analyze_alert(alert):
    text = str(alert.get("message", "")).lower()
    source = alert.get("source", "unknown")
    severity = str(alert.get("severity", "")).lower()

    score = 10
    reasons = []

    if severity in {"critical", "high"}:
        score += 35
        reasons.append("High-severity source alert")

    indicators = {
        "brute force": 30,
        "failed login": 20,
        "port scan": 25,
        "malware": 40,
        "suspicious": 15,
    }

    for indicator, points in indicators.items():
        if indicator in text:
            score += points
            reasons.append(f"Matched indicator: {indicator}")

    score = min(score, 100)

    if score >= 70:
        priority = "HIGH"
    elif score >= 40:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    return {
        "source": source,
        "risk_score": score,
        "priority": priority,
        "reasons": reasons or ["No high-risk indicator matched"],
        "recommended_action": (
            "Validate the alert, investigate related events, preserve evidence, "
            "and escalate according to the SOC playbook."
            if priority != "LOW"
            else "Review context and monitor for additional indicators."
        ),
    }
