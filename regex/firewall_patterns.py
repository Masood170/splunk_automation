patterns = {

    "timestamp": r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})",

    "device": r"\s(FIREWALL)\s",

    "action": r"action=(ALLOW|DENY|DROP|REJECT)",

    "src_ip": r"src=(\d+\.\d+\.\d+\.\d+)",

    "dest_ip": r"dst=(\d+\.\d+\.\d+\.\d+)",

    "src_port": r"sport=(\d+)",

    "dest_port": r"dport=(\d+)",

    "protocol": r"proto=(TCP|UDP|ICMP)",

    "bytes": r"bytes=(\d+)",

    "src_zone": r"src_zone=(\S+)",

    "dest_zone": r"dst_zone=(\S+)",

    "policy_id": r"policy_id=(\d+)"

}