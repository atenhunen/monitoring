"""Simple API emulator."""
import random
import time
import logging
import os

from flask import Flask

app = Flask(__name__)
FORMAT = "%(asctime)-15s %(message)s"
log = logging.getLogger("my-logger")
logging.basicConfig(filename='monitoring.log', level=logging.DEBUG)

handler = logging.FileHandler(
    os.environ.get("LOGFILE", "/tmp/var/log/monitoring.log"))
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
log.addHandler(handler)


@app.route('/ping')
def ping():
    """Ping endpoint.

    This endpoint returns emulated server responses with
    random success and messages. Success rate probablility is weighted.
    """
    wait = float(random.randrange(0, 2000)) / 1000
    time.sleep(wait)
    value = random.randint(0, 100)
    if 0 <= value <= 5:
        message = """Internal Server Error"""
        ret = {"type": "error", "message": message}
        log.error(str(ret))
        return str(ret)
    if 5 < value <= 85:
        message = """Fetching users"""
        ret = {"type": "success", "message": message}
        log.error(str(ret))
        return str(ret)
    if 85 < value <= 95:
        message = """User is trying to fetch past 1 year data."""
        ret = {"type": "info", "message": message}
        log.error(str(ret))
        return str(ret)
    if 95 < value <= 100:
        message = """Infrastructure at peak load"""
        ret = {"type": "debug", "message": message}
        log.error(str(ret))
        return str(ret)
