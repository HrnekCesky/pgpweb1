from bottle import route, request, response, view
from datetime import datetime

@route('/gui/get')
@route('/gui/get/')
@view('api-frontend-getkey')
def gui():
    return dict(
        apipath='/api/getkey'
        )

@route('/gui/add')
@route('/gui/add/')
@view('api-frontend-addkey')
def gui():
    return dict(
        apipath='/api/addkey'
        )

@route('/gui/rem')
@route('/gui/rem/')
@view('api-frontend-remkey')
def gui():
    return dict(
        apipath='/api/remkey'
        )




