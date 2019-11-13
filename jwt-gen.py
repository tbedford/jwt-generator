#!/usr/bin/env python3
import os
import jwt
import time
from uuid import uuid4
from dotenv import load_dotenv
import json

def read_file(filename):
    f = open (filename, mode='r', encoding='utf-8')
    source = f.read()
    f.close()
    return source

load_dotenv('.jwt')
app_id = os.getenv("APP_ID")
private_key_file = os.getenv("PRIVATE_KEY_FILE")
private_key = read_file(private_key_file)
exp = os.getenv("EXPIRY")
sub = os.getenv("SUB")
acl = os.getenv("ACL")

def build_payload (application_id,  **kwargs):
    payload = {}
    payload['application_id'] = application_id
    payload['iat'] = int(time.time())
    payload['jti'] = str(uuid4())
    if "exp" in kwargs:
        exp = kwargs.pop('exp')
        if exp:
            payload['exp'] = int(time.time()) + int(exp)
        else:
            payload['exp'] = int(time.time()) + (15*60) # default to 15 minutes
    for k in kwargs:
        if kwargs[k]:
            if k == 'acl':
                payload[k] = json.loads(kwargs[k]) # In jwt.io acl is JSON object in the valid JWT.
            else:
                payload[k] = kwargs[k]
    return payload

payload = build_payload(app_id, exp=exp, sub=sub, acl=acl) # Add optional custom claims as required
token = jwt.encode(payload, private_key, algorithm='RS256')
j = token.decode(encoding='ascii') # Convert byte string to printable string
print(j)
