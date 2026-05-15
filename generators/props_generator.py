output = """

[firewall]

SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-firewall = firewall_extract



[windows]

SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-windows = windows_extract



[linux]

SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-linux = linux_extract



[routers]

SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-router = router_extract



[switches]

SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-switch = switch_extract



[syslog]

SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-syslog = syslog_extract

"""

with open("output/props.conf", "w") as f:

    f.write(output)

print("props.conf generated successfully")