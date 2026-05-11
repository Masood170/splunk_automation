from faker import Faker
import random

fake = Faker()

actions = ["allowed", "blocked", "denied"]
protocols = ["TCP", "UDP", "ICMP"]
countries = ["US", "IN", "UK", "DE", "AU"]

with open("logs/firewall.log", "w") as f:

    for _ in range(100):

        log = (
            f"{fake.hostname()} "
            f"src_ip={fake.ipv4()} "
            f"dest_ip={fake.ipv4()} "
            f"country={random.choice(countries)} "
            f"src_port={random.randint(1024,65535)} "
            f"dest_port={random.randint(1,65535)} "
            f"action={random.choice(actions)} "
            f"protocol={random.choice(protocols)}"
        )

        f.write(log + "\n")

print("Firewall logs generated")