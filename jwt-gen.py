import os
import jwt
import json
import time
from uuid import uuid4
from dotenv import load_dotenv
import requests

def read_file(filename):
    f = open (filename, mode='r', encoding='utf-8')
    source = f.read()
    f.close()
    return source

load_dotenv()
app_id = os.getenv("APP_ID")
private_key_file = os.getenv("PRIVATE_KEY_FILE")
private_key = read_file(private_key_file)
exp = int(os.getenv("EXPIRY"))
sub = os.getenv("SUB")
acl = os.getenv("ACL")

def build_payload (application_id,  **kwargs):
    payload = {}
    payload['application_id'] = application_id
    payload['iat'] = int(time.time())
    payload['jti'] = str(uuid4())
    if "exp" in kwargs:
        payload['exp'] = int(time.time()) + kwargs.pop('exp')
    else:
        payload['exp'] = int(time.time()) + 15*60
    for k in kwargs:
        payload[k] = kwargs[k]
    return payload

payload = build_payload(app_id, exp=exp)
token = jwt.encode(payload, private_key, algorithm='RS256')

# Testing - Then make a call - retrieve info for all calls https://api.nexmo.com/v1/calls
auth = b'Bearer ' + token
headers = {'Authorization': auth, 'Content-Type': 'application/json'}
r = requests.get('https://api.nexmo.com/v1/calls', headers=headers)
print(r.status_code)
