import bottle
import os
import sys

import routes
import key_management
import gui
import crypt

# --- Move this setup to module-level (OUTSIDE __main__) ---
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')

# Point Bottle to pgpweb1/views
VIEWS_DIR = os.path.join(PROJECT_ROOT, 'views')
if VIEWS_DIR not in bottle.TEMPLATE_PATH:
    bottle.TEMPLATE_PATH.insert(0, VIEWS_DIR)

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    bottle.debug(True)

def wsgi_app():
    return bottle.default_app()

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '80'))
    except ValueError:
        PORT = 80

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        return bottle.static_file(filepath, root=STATIC_ROOT)

    bottle.run(server='wsgiref', host=HOST, port=PORT)