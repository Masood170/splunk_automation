from faker import Faker
import random

fake = Faker()

protocols = ["OSPF", "BGP", "EIGRP"]
states = ["FULL", "ACTIVE", "ESTABLISHED"]

with open("logs/router.log", "w") as f:

    for _ in range(100):

        log = (
            f"RTR{random.randint(1,10)} "
            f"neighbor={fake.ipv4()} "
            f"protocol={random.choice(protocols)} "
            f"state={random.choice(states)}"
        )

        f.write(log + "\n")

print("Router logs generated")