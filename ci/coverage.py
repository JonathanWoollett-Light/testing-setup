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
output = sys.argv[3] # test lcov file
old_lcov = sys.argv[4] # master lcov file

print(f"source: {source}")
print(f"target: {target}")

new_coverage_percent = get_coverage(output)
print("--------------------------------------------------------------")
print(
    f"new_coverage_percent: {new_coverage_percent}%",
)
print("--------------------------------------------------------------")

old_coverage_percent = get_coverage(old_lcov)
print("--------------------------------------------------------------")
print(
    f"old_coverage_percent: {old_coverage_percent}%",
)
print("--------------------------------------------------------------")

if new_coverage_percent < old_coverage_percent:
    raise ("Coverage regression found.")
