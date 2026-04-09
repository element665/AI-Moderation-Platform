def apply_rules(result):
    label = result["label"]
    confidence = result["confidence"]

    if label == "spam":
        return "alert"

    if label == "toxic" and confidence > 0.8:
        return "alert_high"

    return "ignore"