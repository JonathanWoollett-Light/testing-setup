import subprocess
import sys


def get_coverage(file):
    coverage_summary = subprocess.run(
        ["lcov", "--summary", file], capture_output=True
    ).stdout

    lines = iter(coverage_summary.splitlines())
    next(lines)  # Reading tracefile lcov.info
    next(lines)  # Summary coverage rate:
    lines_coverage = str(next(lines))  # lines......: 75.6% (65 of 86 lines)

    coverage_percent = float(
        lines_coverage[lines_coverage.find(":") + 2 : lines_coverage.find("%")]
    )
    return coverage_percent

source = sys.argv[1] # test
target = sys.argv[2] # master
output = sys.argv[3]

print(f"source: {source}")
print(f"target: {target}")

new_coverage_percent = get_coverage(output)
print("--------------------------------------------------------------")
print(
    f"new_coverage_percent: {new_coverage_percent}%",
)
print("--------------------------------------------------------------")

# Stash source coverage
subprocess.run(["git", "stash"])
# Checkout coverage on target
subprocess.run(["git", "checkout", target, output])

old_coverage_percent = get_coverage(output)
print("--------------------------------------------------------------")
print(
    f"old_coverage_percent: {old_coverage_percent}%",
)
print("--------------------------------------------------------------")

# Pop stashed source coverage
subprocess.run(["git", "stash", "pop"], capture_output=True)

if new_coverage_percent < old_coverage_percent:
    raise ("Coverage regression found.")
