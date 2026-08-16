"""
Routes and views for the bottle application.
"""

import os
from bottle import route, view, static_file
from datetime import datetime

# Use an explicit base directory for static files so the app works both
# in Vercel serverless environment and when running locally.
BASE_DIR = os.path.dirname(__file__)

@route('/')
@route('/home')
def home():
    # Serve the index.html located in the package directory
    return static_file("index.html", root=BASE_DIR)


@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )


@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )
