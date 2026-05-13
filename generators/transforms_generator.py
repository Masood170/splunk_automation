output = """

[firewall_extract]

REGEX = .*: (ALLOW|DENY|DROP|REJECT) (TCP|UDP|HTTP|HTTPS|DNS|FTP|ICMP) src (\\w+):(\\d+\\.\\d+\\.\\d+\\.\\d+)/(\\d+) dst (\\w+):(\\d+\\.\\d+\\.\\d+\\.\\d+)/(\\d+) policy=(\\S+) bytes=(\\d+) duration=(\\d+)s

FORMAT = action::$1 protocol::$2 src_zone::$3 src_ip::$4 src_port::$5 dest_zone::$6 dest_ip::$7 dest_port::$8 policy::$9 bytes::$10 duration::$11


[windows_extract]

REGEX = .*EventID=(\\d+).*SubjectUserName=(\\S+).*IpAddress=(\\d+\\.\\d+\\.\\d+\\.\\d+).*LogonType=(\\d+)

FORMAT = eventcode::$1 username::$2 src_ip::$3 logontype::$4


[linux_extract]

REGEX = ^(\\d+-\\d+-\\d+\\s+\\d+:\\d+:\\d+).*sshd\\[(\\d+)\\].*for (\\S+) from (\\d+\\.\\d+\\.\\d+\\.\\d+)

FORMAT = timestamp::$1 pid::$2 username::$3 src_ip::$4


[router_extract]

REGEX = .* (RTR-\\S+) .*Duplicate address (\\d+\\.\\d+\\.\\d+\\.\\d+) on (\\S+), sourced by (\\S+)

FORMAT = hostname::$1 duplicate_ip::$2 interface::$3 mac_address::$4


[switch_extract]

REGEX = (\\S+) interface=(\\S+) status=(\\S+) vlan=(\\d+) mac=(\\S+)

FORMAT = hostname::$1 interface::$2 status::$3 vlan::$4 mac_address::$5

"""

with open("../output/transforms.conf", "w") as f:

    f.write(output)

print("transforms.conf generated successfully")