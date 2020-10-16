import redis

class TokenByRedis(object):
    def __init__(self,src):
        self._server , self._port = src.split(":")

    def lookup(self,token):
        clinet = redis.Redis(host=self._server,prot=self._port)
        stuff = clinet.get('token'+token)
        print(stuff)
        if stuff is None:
            return None
        else:
            (host,port) =stuff.split(":")
            port = port.encode('ascii','ignore')
            return [ host, port]
