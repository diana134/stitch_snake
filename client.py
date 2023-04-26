import requests, configparser

config = configparser.ConfigParser()
config.read('config.ini')

# set up authentication credentials
username = config.get('ravelry', 'authUsername')
password = config.get('ravelry', 'authPassword')

# create a requests session object
session = requests.Session()

# attach the credentials to the session object
session.auth = (username, password)

# make the request
response = session.get('https://api.ravelry.com/patterns/search.json')

# print the response
print(response.text)
