import re
import os

from regex.firewall_patterns import patterns as firewall_patterns
from regex.windows_patterns import patterns as windows_patterns
from regex.linux_patterns import patterns as linux_patterns
from regex.router_patterns import patterns as router_patterns
from regex.switch_patterns import patterns as switch_patterns


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


sources = {

    "FIREWALL": (
        os.path.join(BASE_DIR, "logs", "firewall.log"),
        firewall_patterns
    ),

    "WINDOWS": (
        os.path.join(BASE_DIR, "logs", "windows.log"),
        windows_patterns
    ),

    "LINUX": (
        os.path.join(BASE_DIR, "logs", "linux.log"),
        linux_patterns
    ),

    "ROUTER": (
        os.path.join(BASE_DIR, "logs", "router.log"),
        router_patterns
    ),

    "SWITCH": (
        os.path.join(BASE_DIR, "logs", "switch.log"),
        switch_patterns
    )
}


for source_name, (filepath, patterns) in sources.items():

    print(f"\n{'=' * 15} VALIDATING {source_name} LOGS {'=' * 15}\n")

    try:

        with open(filepath, encoding="utf-8") as f:

            sample = f.readline().strip()

        print("RAW LOG:\n")
        print(sample)

        print("\nEXTRACTED FIELDS:\n")

        for field, pattern in patterns.items():

            match = re.search(pattern, sample)

            if match:

                print(f"{field}: {match.group(1)}")

            else:

                print(f"{field}: NOT FOUND")

    except FileNotFoundError:

        print(f"ERROR: File not found -> {filepath}")

    except Exception as e:

        print(f"ERROR: {str(e)}")

    print("\n")