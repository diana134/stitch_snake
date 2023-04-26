import requests, configparser

class RavelryClient:
    def __init__(self) -> None:
        self.baseUrl = 'https://api.ravelry.com'

        config = configparser.ConfigParser()
        config.read('config.ini')

        # set up authentication credentials
        username = config.get('ravelry', 'authUsername')
        password = config.get('ravelry', 'authPassword')

        # create a requests session object
        self.session = requests.Session()

        # attach the credentials to the session object
        self.session.auth = (username, password)

    def getResource(self, path):
        response =  self.session.get(self.baseUrl + path)
        return response.json()
