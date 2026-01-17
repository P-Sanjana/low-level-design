from ContentServer import ContentServer
from WebServer import WebServer
class BrowserCache(ContentServer):
    def __init__(self):
        self.webServer = None
        self.cache = {}

    def fetchData(self, url):
        if url in self.cache:
            print(f'Loading data from cache')
            return self.cache[url]

        self.webServer = WebServer()
        data = self.webServer.fetchData(url)
        print('Loading data from real server')
        self.cache[url] = data
        return data

