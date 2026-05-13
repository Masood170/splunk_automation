patterns = {

    "timestamp": r"^(\d+-\d+-\d+\s+\d+:\d+:\d+)",

    "process": r"(sshd)",

    "pid": r"sshd\[(\d+)\]",

    "username": r"for\s+(\S+)\s+from",

    "src_ip": r"from\s+(\d+\.\d+\.\d+\.\d+)"
}