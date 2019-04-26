import zerorpc

client = zerorpc.Client()
client.connect("tcp://127.0.0.1:9003")

try:
    client.bad()
except Exception as e:
    print("ERR: %s" % e)