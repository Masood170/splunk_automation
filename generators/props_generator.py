output = """

[firewall_logs]

SHOULD_LINEMERGE = false

REPORT-firewall = firewall_extract


[windows_logs]

SHOULD_LINEMERGE = false

REPORT-windows = windows_extract


[linux_logs]

SHOULD_LINEMERGE = false

REPORT-linux = linux_extract


[routers_logs]

SHOULD_LINEMERGE = false

REPORT-router = router_extract


[switches_logs]

SHOULD_LINEMERGE = false

REPORT-switch = switch_extract

"""

with open("../output/props.conf", "w") as f:

    f.write(output)

print("props.conf generated successfully")