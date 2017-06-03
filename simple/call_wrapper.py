RESTFUL_METHOD=["GET","POST","PUT","PATCH","DELETE"]
class BaseClient(object):
    def __init__(self, endpoint):
        self.url = endpoint
        self.method = None
        self.token = None
    def __getattr__(self, name):
        return WapperObject(name, self)
    def call(self, api, req=None):
        print api
        print req
        print self.method
        pass            
class WapperObject(object):
    def __init__(self, name, proxy, api=None):
        self.name = name
        self.proxy = proxy
        if api is None:
            self.api = '/'+name + "/"
        else:
            self.api = api
    def __getattr__(self, name):
        def call_wrapper(*args, **kwargs):
            if args and kwargs:
                raise ValueError('Not Allow!')
            req = args or kwargs or None
            return self.proxy.call(self.api[:-1], req)
        if name.upper() in RESTFUL_METHOD:
            self.proxy.method = name.upper()
            return call_wrapper
        else:
            self.api = self.api + name + "/"
            return WapperObject(name, self.proxy, self.api)
