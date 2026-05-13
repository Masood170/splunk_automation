patterns = {

    "action": r":\s+(ALLOW|DENY|DROP|REJECT)",

    "protocol": r"(TCP|UDP|HTTP|HTTPS|DNS|FTP|ICMP)",

    "src_zone": r"src\s+(\w+):",

    "src_ip": r"src\s+\w+:(\d+\.\d+\.\d+\.\d+)",

    "src_port": r"src\s+\w+:\d+\.\d+\.\d+\.\d+/(\d+)",

    "dest_zone": r"dst\s+(\w+):",

    "dest_ip": r"dst\s+\w+:(\d+\.\d+\.\d+\.\d+)",

    "dest_port": r"dst\s+\w+:\d+\.\d+\.\d+\.\d+/(\d+)",

    "policy": r"policy=(\S+)",

    "bytes": r"bytes=(\d+)",

    "duration": r"duration=(\d+)s"
}