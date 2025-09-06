import os

hosts = ["8.8.8.8", "1.1.1.1", "192.168.1.1"]

for host in hosts:
    response = os.system(f"ping -c 2 {host}")
    if response == 0:
        print(f"{host} is UP ✅")
    else:
        print(f"{host} is DOWN ❌")
