from bottle import route, request, response
from pathlib import Path

@route('/api')
@route('/api/')
def apilist():
    return {'addkey': '/api/addkey', 'encrypt': '/api/encrypt'}

@route('/api/addkey', method='GET')
@route('/api/addkey/', method='GET')
@route('/api/remkey', method='GET')
@route('/api/remkey/', method='GET')
def addkey_get():
    return {'message': 'Please use POST method to add a key.'}


@route('/api/getkey/<name>', method='POST')
def getkey_post():
    return {'message': 'Please use GET method to get a key.'}

@route('/api/getkey/')
@route('/api/getkey')
def getkey_list():
    return {'keys': [f.name for f in Path('key').glob('*.asc')]}

@route('/api/addkey', method='POST')
@route('/api/addkey/', method='POST')
def addkey_post():
    name = request.forms.get('name')
    key = request.forms.get('key')
    if Path(f"key/{name}-public.asc").exists():
        response.status = 409
        return "Key already exists."
    else: 
        with open(f"key/{name}-public.asc", "x") as f:
            f.write(str(key))
        response.status = 201
        return "Key added successfully."

@route('/api/remkey', method='POST')
@route('/api/remkey/', method='POST')
def remkey_post():
    name = request.forms.get('name')
    if Path(f"key/{name}-public.asc").exists():
        Path(f"key/{name}-public.asc").unlink()
        response.status = 201
        return "Key removed successfully."
    else:
        response.status = 404
        return "Key not found."

@route('/api/getkey/<name>', method='GET')
def getkey_get(name):
    if Path(f"key/{name}-public.asc").exists():
        with open(f"key/{name}-public.asc", "r", encoding="utf-8") as f:
            key = f.read()
        response.content_type = 'application/pgp-keys'
        return key
    else:
        response.status = 404
        return "Key not found."

# import gnupg

# pgp = gnupg.GPG(gnupghome='pgpp')
