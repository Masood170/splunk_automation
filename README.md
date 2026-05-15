# Splunk Parsing Automation Project

## Overview

This project automates Splunk log parsing for multiple enterprise log sources including:

- Firewall Logs
- Windows Logs
- Linux Logs
- Router Logs
- Switch Logs

The project fetches real logs from Splunk, validates regex extraction, and automatically generates:

- props.conf
- transforms.conf

This simulates a real-world Splunk Heavy Forwarder parsing workflow.

---

# Project Architecture

```text
PythonProject1
│
├── logs
│   ├── firewall.log
│   ├── linux.log
│   ├── windows.log
│   ├── router.log
│   ├── switch.log
│   └── remote_splunk.log
│
├── output
│   ├── props.conf
│   └── transforms.conf
│
├── regex
│   ├── firewall_patterns.py
│   ├── linux_patterns.py
│   ├── windows_patterns.py
│   ├── router_patterns.py
│   └── switch_patterns.py
│
├── generators
│   ├── props_generator.py
│   └── transforms_generator.py
│
├── validators
│   └── regex_validator.py
│
├── splunk_log_fetcher.py
├── hec_sender.py
├── ui.py
├── main.py
├── requirements.txt
└── README.md
