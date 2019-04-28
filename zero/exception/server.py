import zerorpc

class ExceptionRPC(object):
    def bad(self):
        raise Exception(":P")

server = zerorpc.Server(ExceptionRPC())
server.bind("tcp://0.0.0.0:9003")
print("server run on localhost:9003")
server.run()