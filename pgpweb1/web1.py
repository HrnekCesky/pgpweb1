from bottle import route, static_file

@route('/neco/<a>')
def neco(a):
    return static_file(f"{a}.html", root="neco")