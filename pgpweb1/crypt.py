from bottle import route, request, response
import requests

import pgpy

BLOB_API_URL = "https://ehvlb7betcblpmyb.public.blob.vercel-storage.com"

@route('/api/encrypt', method='POST')
@route('/api/encrypt/', method='POST')
def encrypt_post():
    name = request.forms.get('name')
    text = request.forms.get('text')
    key = pgpy.PGPKey.from_file(f"{BLOB_API_URL}/{name}.asc")
    out = str(key)
    return f"{out}"