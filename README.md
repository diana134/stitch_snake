# stitch_snake
A Python client for interacting with the Ravelry API.

Create a `config.ini` file like this, where [username] and [password] come from https://www.ravelry.com/pro/developer

```
[ravelry]
authUsername = [username]
authPassword = [password]
```

Usage:
```
client = RavelryClient()
print(client.getResource('/patterns/search.json'))
```