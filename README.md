# jwt-generator

**STATUS:** Working.

A command-line tool for generating JWTs.

## Overview

This is a handy little tool that I use to save time when testing Nexmo projects. I have a lot of small projects and found that during testing generating JWTs is not always convenient on the command line because of escaping and so on. I prefer to have the essential info in a env file that is specific to the project. This makes creating a JWT easy. 

The key point is JWT generation is driven by an environment file. This saves a lot of copying pasting (of APP_ID for example) and escaping on the command line.

## .jwt file

As you may already have a `.env` file in your project, `.jwt` is used by default to contain JWT-related info, although you can change this to be anything you want. It is worth keeping your JWT info in a separate file though, because as some claims are optional you never know what is general config and what is related to JWT in a generic env file. 

``` shell
APP_ID="7ffb050a-121e-4a67-94b8-8301a7e4163d"
PRIVATE_KEY_FILE="private.key"
EXPIRY=36400
...
```

You can configure the `.jwt` file with other claims such as `SUB` and `ACL` (for authenticating users in Client SDK apps). They will automagically be added to the JWT payload.

## Usage

There are various ways to use this. 

1) Set an environment variable:

``` shell
export JWT=`./jwt-gen.py`
```

Will set `JWT` to the token. You can check by using `echo $JWT`.

This is quite convenient but uses environment variables and so maybe not 100% secure. You would also need to maintain multiple JWT env variables and if you switch between multiple projects quite frequently it could be hard to keep track of them all.

2) Copy and paste the generated JWT. 

Not ideal, but you can just copy and paste the JWT output to wherever it needs to go (a Bash shell script using Curl for example).

## Notes

* For Nexmo work (which is primarily what I'm using this for) you don't need ACL and SUB unless you are authenticating users into the Client SDK.
* Expiry is handled this way: if you specify an expiry (I usually set 24 hours for testing convenience) it will be heeded.If it's not specified it will be set to the default of 15 minutes.
* ACL. If you look at valid ACLs for working with Nexmo Client SDK in https://jwt.io you will see they are a JSON object. For this reason I have to convert this from a JSON-type string to a Python object with `json.loads()` - you then have a Python dictionary (`print(type(payload['acl']))`) and `jwt.encode` does the right thing.
* When printing out the JWT it's actually a byte string after encoding, so you need to decode that for the real world using `str.decode()`. I use the ASCII encoding because ASCII chars should cover the range of chars in a JWT (base64url encoded data is a string of characters that only contains `a-z`, `A-Z`, `0-9`, `-` and `_`). 

## TODO

- [x] Tested via jwt.io
- [x] Tested with Voice app
- [x] Tested with RTC app against Conversation API
- [x] Tested `sub` and `acl` with Client SDK apps (using jwt.io)
- [ ] Tested with Messages and Dispatch apps

> **Note**: If you testing validity of your JWT on jwt.io don't forget to paste your **public** key into the correct box in order to verify your JWT signature.

