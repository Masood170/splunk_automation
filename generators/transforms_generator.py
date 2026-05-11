from regex.firewall_patterns import patterns as firewall_patterns
from regex.linux_patterns import patterns as linux_patterns
from regex.windows_patterns import patterns as windows_patterns
from regex.pan_patterns import patterns as pan_patterns
from regex.switch_patterns import patterns as switch_patterns
from regex.router_patterns import patterns as router_patterns

all_patterns = {
    "firewall": firewall_patterns,
    "linux": linux_patterns,
    "windows": windows_patterns,
    "pan": pan_patterns,
    "switch": switch_patterns,
    "router": router_patterns
}

output = []

for source, patterns in all_patterns.items():

    for field, regex in patterns.items():

        stanza = f"""
[{source}_{field}]
REGEX = {regex}
FORMAT = {field}::$1
"""

        output.append(stanza)

with open("output/transforms.conf", "w") as f:

    f.write("\n".join(output))

print("transforms.conf generated")