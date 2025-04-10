#Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.
import json

import os

file_path = os.path.join(os.path.dirname(__file__), "sample-data.json")

with open(file_path, "r") as file:
    data = json.load(file)

interfaces = data["imdata"]

print("Interface Status")
print("=" * 90)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 90)

for interface in interfaces:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else ""
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")