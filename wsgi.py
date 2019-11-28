"""wsgi.py."""
import sys

from monitoring.server import app as app

if __name__ == "__main__":
    """Main."""
    app.run(sys.argv)
