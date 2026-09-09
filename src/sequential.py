KEYWORDS = {
    "errors": "ERROR",
    "critical": "CRITICAL",
    "failed_logins": "Failed login",
    "unauthorized": "Unauthorized",
    "sql_errors": "SQL error",
    "connection_refused": "Connection refused",
}


def empty_result():
    return {
        "total_lines": 0,
        "errors": 0,
        "critical": 0,
        "failed_logins": 0,
        "unauthorized": 0,
        "sql_errors": 0,
        "connection_refused": 0,
    }


def analyze_sequential(logs):
    result = empty_result()

    for line in logs:
        result["total_lines"] += 1

        for key, keyword in KEYWORDS.items():
            if keyword.lower() in line.lower():
                result[key] += 1

    return result
