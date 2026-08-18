from bottle import route, request, response
import requests

import pgpy

BLOB_API_URL = "https://ehvlb7betcblpmyb.public.blob.vercel-storage.com"

@route('/api/encrypt', method='POST')
@route('/api/encrypt/', method='POST')
def encrypt_post():
    name = request.forms.get('name')
    text = request.forms.get('text')
    #get stuff 
    public_key = pgpy.PGPKey.from_blob(str(requests.get(f"{BLOB_API_URL}/{name}.asc").text))
    message = pgpy.PGPMessage.new(str(text))
    #encrypt text
    out = public_key[0].encrypt(message)
    return f"{out}"