"""Simple API emulator."""
import random
import time

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """Index."""
    return 'Server online'


@app.route('/ping')
def ping():
    """Ping."""
    wait = float(random.randrange(0, 2000)) / 1000
    time.sleep(wait)
    value = random.randint(0, 100)
    if 0 <= value <= 5:
        return """{"type": "error", "message": "Internal Server Error"}"""
    if 5 < value <= 85:
        return """{"type": "success", "message": "Fetching users"}"""
    if 85 < value <= 95:
        return """{
            "type": "info",
            "message": "User is trying to fetch past 1 year data."}"""
    if 95 < value <= 100:
        return """{"type": "debug",
            "message": "Infrastructure at peak load"}"""
