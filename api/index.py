"""
Vercel entrypoint for the Bottle WSGI app.
This file exposes a WSGI `app` object which the @vercel/python builder can use.
It ensures the application package (pgpweb1) is on sys.path and imports the app
so routes are registered.
"""
import os
import sys

# Ensure the pgpweb1 package directory is importable
PROJECT_ROOT = os.path.join(os.getcwd(), "pgpweb1")
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Import the application module to register routes and handlers.
# The project's app.py registers routes on bottle.default_app().
try:
    import app as _app_module  # noqa: F401
except Exception:
    # Try importing as package-style if repository structure differs
    import pgpweb1.app as _app_module  # noqa: F401

from bottle import default_app

# Expose WSGI app variable that Vercel's python builder can use.
app = default_app()
