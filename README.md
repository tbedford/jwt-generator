# jwt-generator

A command-line tool for generating JWTs.

The key point is JWT generation is driven by a `.env` file. This saves a lot of copying pasting (of APP_ID for example) and escaping on the command line.

## Usage

There are various ways to use this. 

1) Via an environment variable:

``` shell
export JWT=`./jwt-gen.py`
```

This is quite convenient but uses environment variables. You would also need to maintain multiple JWT env variables if you switch between multiple projects quite frequently.

2) Copy and paste. Not ideal, but you can just copy and paste the JWT output to wherever it needs to go (a Bash shell script using Curl for example).

## .env file

``` shell
APP_ID="7ffb050a-121e-4a67-94b8-8301a7e4163d"
PRIVATE_KEY_FILE="private.key"
EXPIRY=38400
...
```

You can configure the `.env` file with other claims such as `SUB` and `ACL` (for Client SDK apps). They will automagically be added to the JWT payload.


