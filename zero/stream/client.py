import zerorpc

client = zerorpc.Client()
client.connect("tcp://127.0.0.1:9002")

for item in client.streaming_range(10,20,2):
    print("%d " % item)