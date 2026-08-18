from bottle import route, request, response, view
from datetime import datetime

@route('/gui')
@route('/gui/')
@view('api-frontend')
def gui():
    return dict(
        title='PGP Web GUI',
        body='<a href="/gui/get">Get Key</a><br> <a href="/gui/add">Add Key</a><br> <a href="/gui/rem">Remove Key</a><br>'
        )


@route('/gui/get')
@route('/gui/get/')
@view('api-frontend-getkey')
def get():
    return dict(
        apipath='/api/getkey'
        )

@route('/gui/add')
@route('/gui/add/')
@view('api-frontend-addkey')
def add():
    return dict(
        apipath='/api/addkey'
        )

@route('/gui/rem')
@route('/gui/rem/')
@view('api-frontend-remkey')
def rem():
    return dict(
        apipath='/api/remkey'
        )




