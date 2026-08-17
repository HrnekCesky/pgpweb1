from bottle import route, request, response, view
from datetime import datetime

@route('/gui')
@route('/gui')
@view('api-frontend')
def gui():
    """Renders the GUI page."""
    return dict(
        title='GUI',
        message='Your GUI page.',
        year=datetime.now().year
    )