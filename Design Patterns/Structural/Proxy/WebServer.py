from datetime import datetime
from ContentServer import ContentServer
import time
class WebServer(ContentServer):
    def fetchData(self, url):
        print(f'Fetching data from ${url}')
        time.sleep(1)
        return f'Fetched data: Hello World! from {url} at {datetime.today()}'
