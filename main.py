import os

print("\nValidating Regex Extraction...\n")

os.system("python validators/regex_validator.py")

print("\nGenerating transforms.conf...\n")

os.system("python generators/transforms_generator.py")

print("\nGenerating props.conf...\n")

os.system("python generators/props_generator.py")

print("\nReal Splunk Parsing Automation Completed Successfully")