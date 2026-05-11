import re

from regex.firewall_patterns import patterns as firewall_patterns
from regex.linux_patterns import patterns as linux_patterns
from regex.windows_patterns import patterns as windows_patterns
from regex.pan_patterns import patterns as pan_patterns
from regex.switch_patterns import patterns as switch_patterns
from regex.router_patterns import patterns as router_patterns

sources = {

    "firewall": ("logs/firewall.log", firewall_patterns),

    "linux": ("logs/linux.log", linux_patterns),

    "windows": ("logs/windows.log", windows_patterns),

    "pan": ("logs/pan.log", pan_patterns),

    "switch": ("logs/switch.log", switch_patterns),

    "router": ("logs/router.log", router_patterns)
}

for source, (logfile, patterns) in sources.items():

    print(f"\n========== VALIDATING {source.upper()} LOGS ==========\n")

    with open(logfile) as f:

        sample = f.readline()

    print("Sample Log:\n")

    print(sample)

    print("\nExtracted Fields:\n")

    for field, pattern in patterns.items():

        match = re.search(pattern, sample)

        if match:

            print(f"{field}: {match.group(1)}")

        else:

            print(f"{field}: NOT FOUND")