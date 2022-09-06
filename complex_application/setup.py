import subprocess
DEPENDENCIES = ["gcc","python3"]

# Check dependencies
def check(x):
    return subprocess.run(["dpkg","-l",x],capture_output=True).returncode
def install(x):
    return subprocess.run(["sudo","apt-get","install","-y",x]).returncode

for dependency in DEPENDENCIES:
    print(dependency)
    print("│ checking")
    print("┊")
    # Check if dependency installed
    if check(dependency):
        print("┊")
        print("│ missing")
        # Install dependencies
        choice = input(f"│ run `apt-get install {dependency}` [yes/*]? ")
        if choice == "yes":
            print("│ installing")
            print("┊")
            status = install(dependency)
            print("┊")
            print("│ installed")
        else:
            print("│ skipping")
    else:
        print("┊")
        print("│ found")
    print("└")