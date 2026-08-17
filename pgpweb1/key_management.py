from bottle import route, request, response
from pathlib import Path
import requests
import os

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


BLOB_TOKEN = os.environ.get("BLOB_READ_WRITE_TOKEN")
BLOB_API_URL = "https://vxwwmkyy1varceo3.private.blob.vercel-storage.com"

@route('/api/getkey/')
@route('/api/getkey')
def getkey_list():
    return #todoooooo (list all keys in the key directory)

# @route('/api/addkey', method='POST')
# @route('/api/addkey/', method='POST')
# def addkey_post():
#     name = request.forms.get('name')
#     key = request.forms.get('key')
#     if False: #todoooooo (path exists)
#         #todoooooo (create the key and write it)
#         response.status = 409
#         return "Key already exists."
#     else: 
#         #todoooooo
#         response.status = 201
#         return "Key added successfully."

@route('/api/addkey', method='POST')
@route('/api/addkey/', method='POST')
def addkey_post():
    name = request.forms.get('name')
    key = request.forms.get('key')
    filename = f"key/{name}-public.asc"

    if not BLOB_TOKEN:
        response.status = 500
        return "Blob storage token not configured."

    # Upload file directly to Vercel Blob
    headers = {
        "authorization": f"Bearer {BLOB_TOKEN}",
        "x-add-random-suffix": "false"  # Keeps the exact filename
    }
    
    blob_response = requests.put(
        f"{BLOB_API_URL}/{filename}",
        data=str(key),
        headers=headers
    )

    if blob_response.status_code in (200, 201):
        data = blob_response.json()
        response.status = 201
        return {"status": "success", "url": data.get("url")}
    else:
        response.status = blob_response.status_code
        return blob_response.text

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