import subprocess
import sys

source = sys.argv[1] # test
target = sys.argv[2] # master

print(f"source: {source}")
print(f"target: {target}")

# Checkout branch
# We can skip this step as we presume we are already checked out on this.
# subprocess.run(["git", "checkout", source])

# Benchmark branch
subprocess.run(
    ["cargo", "bench", "--bench", "benchmark", "--", "--save-baseline", "source"]
)
# Checkout master
subprocess.run(["git", "checkout", target])
# Benchmark master
subprocess.run(
    ["cargo", "bench", "--bench", "benchmark", "--", "--save-baseline", "target"]
)
# Compare benchmarks
subprocess.run(
    [
        "cargo",
        "bench",
        "--bench",
        "benchmark",
        "--",
        "--load-baseline",
        "target",
        "--baseline",
        "source",
    ]
)

import os
import json

# We require a 10% performance decrease before we consider it a regression.
MARGIN = 0.10
changes = {}
regressions = {}
for fn in os.listdir("./target/criterion"):
    change_file = open(f"./target/criterion/{fn}/change/estimates.json", "r")
    change_json = json.loads(change_file.read())
    change_mean = change_json["mean"]["point_estimate"]

    changes[fn] = change_mean
    if change_mean > MARGIN:
        regressions[fn] = change_mean

print(f"Changes: {changes}")
print(f"Regressions: {regressions}")


# Re-checkout target
subprocess.run(["git", "checkout", target])

if len(regressions) > 0:
    raise ("Regressions found.")
