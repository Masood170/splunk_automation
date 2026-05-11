from faker import Faker
import random

fake = Faker()

actions = ["allow", "deny"]

with open("logs/pan.log", "w") as f:

    for _ in range(100):

        log = (
            f"TRAFFIC start "
            f"src={fake.ipv4()} "
            f"dst={fake.ipv4()} "
            f"sport={random.randint(1000,65535)} "
            f"dport={random.randint(1,65535)} "
            f"action={random.choice(actions)}"
        )

        f.write(log + "\n")

print("PAN logs generated")