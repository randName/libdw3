from json import loads, dumps
from urllib.request import urlopen, Request


class FirebaseApplication():

    def __init__(self, url, token):
        self.url = "%s{}.json?auth=%s" % (url, token)

    def request(self, method, node, data=None):
        request = Request(self.url.format(node), method=method)
        if data:
            request.data = dumps(data).encode()
            request.add_header('Content-Type', 'application/json')
        result = urlopen(request)

        if data:
            return "OK" if result.getcode() == 200 else "ERROR"
        else:
            return loads(result.read().decode())

    def put(self, root, node, data):
        return self.request('PUT', root+node, data)

    def post(self, newnode, data):
        return self.request('POST', newnode, data)

    def get(self, node):
        return self.request('GET', node)
