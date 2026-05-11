from faker import Faker
import random

fake = Faker()

with open("logs/linux.log", "w") as f:

    for _ in range(100):

        log = (
            f"Aug 10 10:15:22 "
            f"{fake.hostname()} "
            f"sshd[{random.randint(1000,9999)}]: "
            f"Failed password for root "
            f"from {fake.ipv4()} "
            f"port 22"
        )

        f.write(log + "\n")

print("Linux logs generated")