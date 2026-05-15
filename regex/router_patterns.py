patterns = {

    "timestamp": r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})",

    "hostname": r"(RTR-\S+)",

    "protocol": r"%(BGP|OSPF|EIGRP|RIP|ISIS)-",

    "interface": r":\s+(\S+)\s+Peer",

    "peer_ip": r"Peer\s+(\d+\.\d+\.\d+\.\d+)",

    "message": r"-\s+(.*?)\s+AS\d+",

    "asn": r"AS(\d+)"

}