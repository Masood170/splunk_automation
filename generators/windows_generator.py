from faker import Faker
import random

fake = Faker()

with open("logs/windows.log", "w") as f:

    for _ in range(100):

        log = (
            f"EventCode=4625 "
            f"AccountName=Administrator "
            f"SourceNetworkAddress={fake.ipv4()} "
            f"LogonType={random.randint(1,10)}"
        )

        f.write(log + "\n")

print("Windows logs generated")