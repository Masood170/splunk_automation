patterns = {

    "logtype": r"^(TRAFFIC)",

    "src_ip": r"src=(\d+\.\d+\.\d+\.\d+)",

    "dest_ip": r"dst=(\d+\.\d+\.\d+\.\d+)",

    "src_port": r"sport=(\d+)",

    "dest_port": r"dport=(\d+)",

    "action": r"action=(\S+)"
}