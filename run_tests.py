import argparse
import subprocess
import sys
import time


def run_pytest(args_list):
    print(f"Running pytest with args: {' '.join(args_list)}")
    result = subprocess.run(["pytest"] + args_list)
    sys.exit(result.returncode)


def main():
    parser = argparse.ArgumentParser(description="Run tests dynamically.", add_help=True)
    parser.add_argument("--mode", required=True, choices=["ALL", "FLOW", "COMPONENT", "PRIORITY"])
    parser.add_argument("--flow")
    parser.add_argument("--component")
    parser.add_argument("--priority")

    # This line allows unknown args like --alluredir to pass through
    args, unknown = parser.parse_known_args()

    if args.mode == "ALL":
        run_pytest(["tests/"] + unknown)

    elif args.mode == "FLOW":
        if not args.flow:
            print("Error: --flow is required for mode FLOW")
            sys.exit(1)
        run_pytest([f"tests/test_{args.flow}.py"] + unknown)

    elif args.mode == "COMPONENT":
        if not args.flow or not args.component:
            print("Error: --flow and --component are required for mode COMPONENT")
            sys.exit(1)
        run_pytest([
                       f"tests/test_{args.flow}.py",
                       "-m", args.component
                   ] + unknown)

    elif args.mode == "PRIORITY":
        if not args.priority:
            print("Error: --priority is required for mode PRIORITY")
            sys.exit(1)
        run_pytest([
                       "tests/",
                       "-m", args.priority
                   ] + unknown)


if __name__ == "__main__":
    main()
    time.sleep(600)
