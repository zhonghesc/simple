from simple.call_wrapper import BaseClient
class Client(BaseClient):
    def call(self, api, req):
        print api
        print req
        print self.method

client = Client("http://127.0.0.1:8080/")
client.api.v1.user.auth.get(data="aaaa")
client.api.v1.user.auth.post(data="aaaa")
client.api.v1.user.auth.delete(data="aaaa")
client.api.v1.user.auth.put(data="aaaa")
