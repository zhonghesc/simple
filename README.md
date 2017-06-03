# simple
simple code for restful API

#API:
#    GET /xxx/xxx/xxx/xxx
#example:
#client = ProxyClient(endpoint)
#s.xxx.xxx.xxx.xxx.request(params)

TEST:
>>>s = ProxyClient("http://127.0.0.1:8080")
>>>data={"aa":"bb"}
>>>headers={"ContentType":"application/json"}
>>>params = {"user":"xxxxxx"}
>>>s.api.v1.test.auth.request(headers=headers, data=data, method='GET', params=params)

