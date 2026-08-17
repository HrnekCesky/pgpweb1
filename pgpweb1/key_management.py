from bottle import route, request, response
from pathlib import Path
import vercel_blob as blob

BLOB_API_URL = "https://vxwwmkyy1varceo3.private.blob.vercel-storage.com"

#fail scenarios
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

#success scenarios
@route('/api/getkey/')
@route('/api/getkey')
def getkey_list():
    return #todoooooo (list all keys in the key directory)

@route('/api/addkey', method='POST')
@route('/api/addkey/', method='POST')
def addkey_post():
    name = request.forms.get('name')
    key = request.forms.get('key')
    if False: #todoooooo (path exists)
        #todoooooo
        response.status = 409
        return "Key already exists."
    else: 
        #todoooooo (create the key and write it)
        out = blob.put(f"{name}", key.encode('utf-8'))
        response.status = 201
        return f"Key added successfully. {out}"

@route('/api/remkey', method='POST')
@route('/api/remkey/', method='POST')
def remkey_post():
    name = request.forms.get('name')
    if False: #todoooooo (path exists)
        #todoooooo (remove the key)
        response.status = 201
        return "Key removed successfully."
    else:
        response.status = 404
        return "Key not found."

@route('/api/getkey/<name>', method='GET')
def getkey_get(name):
    if False: #todoooooo (path exists)
        #todoooooo (read the key from the file)
        response.content_type = 'application/pgp-keys'
        return key
    else:
        response.status = 404
        return "Key not found."