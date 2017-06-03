class ProxyClient(object):
    def __init__(self, endpoint):
        self.url = endpoint
        self.token = None
    def __getattr__(self, name):
        return WapperObject(name, self)
    def call(self, api, req=None):
        url = self.url+api
        token = self.token
        params = req.get("params")
        data = req.get("data")
        headers = req.get("headers")
        print params
        print data
        print headers

        return None
class WapperObject(object):
    def __init__(self, name, proxy, api=None):
        self.name = name
        self.proxy = proxy
        if api is None:
            self.api = '/'
        else:
            self.api = api
    def __getattr__(self, name):
        def call_wrapper(*args, **kwargs):
            if args and kwargs:
                raise ValueError('Not Allow!')
            req = args or kwargs or None
            api=self.api[:-1]
            return self.proxy.call(api, req)
        if name == 'request':
            return call_wrapper
        else:
            self.api = self.api + name + "/"
            return WapperObject(name, self.proxy, self.api)

s = ProxyClient("http://127.0.0.1:8080")
data={"aa":"bb"}
headers={"ContentType":"application/json"}
params = {"user":"xxxxxx"}

s.aa.bb.cc.dd.ff.request(headers=headers, data=data, method='GET', params=params)
