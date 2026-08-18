from bottle import route, request, response, view

@route('/gui')
@route('/gui/')
@view('api-frontend')
def gui():
    return dict(
        title='PGP Web GUI',
        base='<a href="/gui/get">Get Key</a><br> <a href="/gui/add">Add Key</a><br> <a href="/gui/rem">Remove Key</a><br>'
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

@route('/gui/encrypt')
@route('/gui/encrypt/')
@view('api-frontend-encrypt')
def encrypt():
    return dict(
        apipath='/api/encrypt'
        )

