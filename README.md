=============
simple
=============
simple code for restful API

RESTFUL API
----------
    GET /xxx/xxx/xxx/xxx

Usage
----------

example:
    >>>s = ProxyClient("http://127.0.0.1:8080")
    >>>data={"aa":"bb"}
    >>>headers={"ContentType":"application/json"}
    >>>params = {"user":"xxxxxx"}
    >>>s.api.v1.test.auth.request(headers=headers, data=data, method='GET', params=params)

