from faker import Faker
import random

fake = Faker()

statuses = ["up", "down"]

with open("logs/switch.log", "w") as f:

    for _ in range(100):

        log = (
            f"SW{random.randint(1,10)} "
            f"interface=Gig0/{random.randint(1,48)} "
            f"status={random.choice(statuses)} "
            f"vlan={random.randint(1,100)} "
            f"mac={fake.mac_address()}"
        )

        f.write(log + "\n")

print("Switch logs generated")