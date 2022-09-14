import subprocess
import sys

source = sys.argv[1]
target = sys.argv[2]

print(f"source: {source}")
print(f"target: {target}")

# Checkout target
# We can skip this step as we presume we are already checked out on this.
# subprocess.run(["git","checkout","target"])
# Benchmark target
subprocess.run(["cargo","bench","--bench", "benchmark", "--", "--save-baseline", "target"])
# Checkout source
subprocess.run(["git","checkout",source])
# Benchmark source
subprocess.run(["cargo","bench","--bench", "benchmark", "--", "--save-baseline", "source"])
# Compare benchmarks
subprocess.run(["cargo","bench","--bench", "benchmark", "--", "--load-baseline","target","--baseline","source"])

import os
import json

# We require a 10% performance decrease before we consider it a regression.
MARGIN = 0.10
changes = {}
regressions = {}
for fn in os.listdir("./target/criterion"):
    change_file = open(f"./target/criterion/{fn}/change/estimates.json","r")
    change_json = json.loads(change_file.read())
    change_mean = change_json["mean"]["point_estimate"]

    changes[fn] = change_mean
    if change_mean > MARGIN:
        regressions[fn] = change_mean

print(f"Changes: {changes}")
print(f"Regressions: {regressions}")

if len(regressions) > 0:
    raise("Regressions found.")