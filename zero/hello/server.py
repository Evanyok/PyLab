import zerorpc

class HiRPC(object):
    def hi(self, sth):
        return "hi, %s" % sth

server = zerorpc.Server(HiRPC())
server.bind("tcp://0.0.0.0:9001")
print("server run on localhost:9001")
server.run()