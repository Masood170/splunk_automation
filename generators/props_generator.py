props = """
[firewall_logs]
SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-firewall = firewall_extract

[linux_logs]
SHOULD_LINEMERGE = false
REPORT-linux = linux_extract

[windows_logs]
SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-windows = windows_extract

[pan_logs]
SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-pan = pan_extract

[switch_logs]
SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-switch = switch_extract

[router_logs]
SHOULD_LINEMERGE = false
KV_MODE = none
REPORT-router = router_extract
"""

with open("output/props.conf", "w") as f:

    f.write(props)

print("props.conf generated")