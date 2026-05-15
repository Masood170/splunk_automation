patterns = {

    "timestamp": r"^(\w+\s+\d+\s+\d+:\d+:\d+)",

    "hostname": r"^\w+\s+\d+\s+\d+:\d+:\d+\s+(\S+)",

    "process": r"\s(\w+)\[(\d+)\]:",

    "pid": r"\[(\d+)\]:",

    "log_level": r"\[(INFO|WARN|ERROR|DEBUG|CRIT)\]",

    "facility": r"\[(auth|daemon|cron|kern|syslog|user)\]",

    "username": r"user\s+(\S+)|USER=(\S+)|for\s+(\S+)",

    "src_ip": r"from\s+(\d+\.\d+\.\d+\.\d+)",

    "message": r":\s+\[.*?\]\s+\[.*?\]\s+(.*)"

}