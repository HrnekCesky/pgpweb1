from bottle import route, request, response, view
import requests

import pgpy

BLOB_API_URL = "https://ehvlb7betcblpmyb.public.blob.vercel-storage.com"

@route('/api/encrypt', method='POST')
@route('/api/encrypt/', method='POST')
@view('api-frontend')
def encrypt_post():
    name = request.forms.get('name')
    text = request.forms.get('text')
    #get stuff 
    public_key, _ = pgpy.PGPKey.from_blob(str(requests.get(f"{BLOB_API_URL}/{name}.asc").text))
    message = pgpy.PGPMessage.new(str(text))
    #encrypt text
    out = public_key.encrypt(message)
    return dict(
        title='Encrypted Message',
        base=f'<pre>{out}</pre>'
    )

@route('/api/sign', method='POST')
@route('/api/sign/', method='POST')
@view('api-frontend-sign')
def sign_post():
    name = request.forms.get('name')
    text = request.forms.get('text')
    #get stuff 
    private_key, _ = pgpy.PGPKey.from_blob(str(requests.get(f"{BLOB_API_URL}/{name}.asc").text))
    message = pgpy.PGPMessage.new(str(text))
    #sign text
    out = private_key.sign(message)
    return dict(
        title='Signed Message',
        base=f'<pre>{out}</pre>'
    )