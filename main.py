import os

print("\nGenerating Firewall Logs...\n")
os.system("python generators/firewall_generator.py")

print("\nGenerating Linux Logs...\n")
os.system("python generators/linux_generator.py")

print("\nGenerating Windows Logs...\n")
os.system("python generators/windows_generator.py")

print("\nGenerating PAN Logs...\n")
os.system("python generators/pan_generator.py")

print("\nGenerating Switch Logs...\n")
os.system("python generators/switch_generator.py")

print("\nGenerating Router Logs...\n")
os.system("python generators/router_generator.py")

print("\nGenerating transforms.conf...\n")
os.system("python generators/transforms_generator.py")

print("\nGenerating props.conf...\n")
os.system("python generators/props_generator.py")

print("\nValidating Regex Extractions...\n")
os.system("python validators/regex_validator.py")

print("\nEnterprise Splunk Automation Completed Successfully")