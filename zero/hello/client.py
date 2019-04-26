import zerorpc

client = zerorpc.Client()
client.connect("tcp://127.0.0.1:9001")
print(client.hi("RPC"))