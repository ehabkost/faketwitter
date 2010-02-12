
from twisted.web.resource import Resource

class ApiResource(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.isLeaf = True

    def render_GET(self, request):
        return "ok"

class TwitterResource(Resource):
    def __init__(self, server):
        Resource.__init__(self)
        self.tw_server = server
        self.putChild('api', ApiResource())
