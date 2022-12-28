import subprocess
import re

DIR = "./tmp"

# Download flame graph utils
subprocess.run(
    args=[
        "wget",
        "https://raw.githubusercontent.com/brendangregg/FlameGraph/master/stackcollapse-perf.pl",
    ]
)
subprocess.run(
    args=[
        "wget",
        "https://raw.githubusercontent.com/brendangregg/FlameGraph/master/flamegraph.pl",
    ]
)

# Build test executables
process = subprocess.run(args=["cargo", "test", "--no-run"], capture_output=True)
stderr = process.stderr.decode("utf-8")
# Find test executables
binaries = re.findall(
    " *Executable .*?\.rs \((target\/debug\/deps\/(.*?)-.*?)\)", stderr
)
# For each executable
for path, name in binaries:
    record_output = f"{DIR}/{name}.data"
    # `perf record` the executable
    process = subprocess.run(
        args=["sudo", "perf", "record", "-g", "-o", record_output, f"./{path}"]
    )
    # `perf script` the data
    script_output = f"{DIR}/{name}.perf"
    process = subprocess.run(
        args=["sudo", "perf", "script", "-i", record_output], capture_output=True
    )
    file = open(script_output, "w")
    file.write(process.stdout.decode("utf-8"))
    # `stackcollapse-perf.pl`
    
    # `flamegraph.pl`

# print("group:",out.group(0))
# print("group:",out.group(1))
# print("group:",out.group(2))
# print("group:",out.group(3))
# print("group:",out.group(4))
# for line in stderr.split(b'\n'):
#     print(";line:")
#     # stripped = line.strip()
#     # print("stripped:",stripped)
#     # if stripped[0:] == b""
