import subprocess

# Checkout master
subprocess.run(["git","checkout","master"])
# Benchmark master
subprocess.run(["cargo","bench","--bench", "benchmark", "--", "--save-baseline", "master"])
# Checkout this
subprocess.run(["git","checkout","test"])
# Benchmark this
subprocess.run(["cargo","bench","--bench", "benchmark", "--", "--save-baseline", "test"])
# Compare benchmarks
subprocess.run(["cargo","bench","--bench", "benchmark", "--", "--load-baseline","test","--baseline","master"])

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