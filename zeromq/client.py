import zmq 

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:9000")

for request in range(10):
    socket.send(b"Hi")

    msg = socket.recv_string()
    print("recv: %s" % msg)