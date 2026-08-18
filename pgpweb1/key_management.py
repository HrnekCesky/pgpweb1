from bottle import route, request, response
import vercel_blob as blob

BLOB_API_URL = "https://ehvlb7betcblpmyb.public.blob.vercel-storage.com"

#fail scenarios
@route('/api')
@route('/api/')
def apilist():
    return {'addkey': '/api/addkey', 'encrypt': '/api/encrypt', 'getkey': '/api/getkey', 'remkey': '/api/remkey'}

@route('/api/addkey', method='GET')
@route('/api/addkey/', method='GET')
@route('/api/remkey', method='GET')
@route('/api/remkey/', method='GET')
def addkey_get():
    return {'message': 'Please use POST method to add a key.'}


# @route('/api/getkey/<name>', method='POST')
# @route('/api/getkey/<name>/', method='POST')
# def getkey_post(name):
#     return {'message': 'Please use GET method to get a key.'}

#success scenarios

@route('/api/addkey', method='POST')
@route('/api/addkey/', method='POST')
def addkey_post():
    name = request.forms.get('name')
    key = request.forms.get('key')
    try:
        blob.head(f"{name}.asc") == Exception
        out = blob.put(f"{name}.asc", key.encode('utf-8'))
        response.status = 201
        return f"Key added successfully. {out}"
    except Exception as a:
        response.status = 409
        return f"Key already exists. {a}"

@route('/api/remkey', method='POST')
@route('/api/remkey/', method='POST')
def remkey_post():
    name = request.forms.get('name')
    if blob.head(f"{name}.asc") != Exception:
        out = blob.delete(f"{name}.asc")
        response.status = 201
        return f"Key removed successfully. {out}"
    else:
        response.status = 404
        return "Key not found."

@route('/api/getkey', method='POST')
@route('/api/getkey/', method='POST')
def getkey_get():
    name = request.forms.get('name')
    if name == None:
        #return blob.list()
        return {'message': 'Please provide a key name to retrieve.'}
    if blob.head(f"{name}.asc") != Exception:
        out = blob.head(f"{name}.asc")
        return out
    else:
        response.status = 404
        return "Key not found."