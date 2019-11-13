# jwt-generator

**STATUS:** Working.

A command-line tool for generating JWTs.

The key point is JWT generation is driven by an environment file. This saves a lot of copying pasting (of APP_ID for example) and escaping on the command line.

## .jwt file

As you may already have a `.env` file in your project, `.jwt` is used by default to contain JWT-realted info, although you can change this to be anything you want. It is worth keeping your JWT info in a separate file though, because as some claims are optional you never know what is general config and what is related to JWT in a generic env file. 

``` shell
APP_ID="7ffb050a-121e-4a67-94b8-8301a7e4163d"
PRIVATE_KEY_FILE="private.key"
EXPIRY=36400
...
```

You can configure the `.jwt` file with other claims such as `SUB` and `ACL` (for authneticating users in Client SDK apps). They will automagically be added to the JWT payload.


## Usage

There are various ways to use this. 

1) Via an environment variable:

``` shell
export JWT=`./jwt-gen.py`
```

Will set `$JWT` to the token. You can check by using `echo $JWT`.

This is quite convenient but uses environment variables and so maybe not 100% secure. You would also need to maintain multiple JWT env variables and if you switch between multiple projects quite frequently it could be hard to keep track of them all.

2) Copy and paste the generated JWT. 

Not ideal, but you can just copy and paste the JWT output to wherever it needs to go (a Bash shell script using Curl for example).

## TODO

- [x] Tested via jwt.io
- [x] Tested with Voice app
- [x] Tested with RTC app against Conversation API
- [x] Tested `sub` and `acl` with Client SDK apps (using jwt.io)
- [ ] Tested with Messages and Dispatch apps

> **Note**: If you testing validity of your JWT on jwt.io don't forget to paste your **public** key into the correct box in order to verify your JWT signature.

