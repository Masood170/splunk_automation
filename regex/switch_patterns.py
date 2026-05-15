patterns = {

    "timestamp": r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})",

    "hostname": r"(SW-CORE-\d+)",

    "interface": r"Interface\s+(\S+)",

    "vlan": r"VLAN\s+(\d+)",

    "message": r"VLAN\s+\d+\s+-\s+(.*?)\s+\[Uptime:",

    "uptime": r"\[Uptime:\s+([^\]]+)\]"

}