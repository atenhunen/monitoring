"""Simple API testing importing the requests library."""
import requests
import random
import time
import threading
import sys

# api-endpoint
URL = "http://localhost:5000/ping"


def run_user(loop_max):
    """Mock user sending requests."""
    loop = 0
    while loop < loop_max:
        wait = float(random.randrange(0, 5000)) / 1000
        time.sleep(wait)
        r = requests.get(url=URL)
        data = r._content
        loop = loop + 1
        print(data)


def main():
    """Main."""
    loop_max = 10
    if len(sys.argv) < 2:
        users = 1

    elif sys.argv[1] is not None:
        users = sys.argv[1]
    else:
        users = 1
    if len(sys.argv) > 2:
        loop_max = sys.argv[2]
    threads = []
    for user in range(0, int(users)):
        print("Starting new user %s" % str(user))
        thread = threading.Thread(target=run_user, args=(int(loop_max), ))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
