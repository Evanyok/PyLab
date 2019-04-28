import zerorpc

class StreamingRPC(object):

    @zerorpc.stream
    def streaming_range(self, fr, to, step):
        return range(fr, to, step)

server = zerorpc.Server(StreamingRPC())
server.bind("tcp://0.0.0.0:9002")
print("server run on localhost:9002")
server.run()
