import time 
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:9000")

while True:
    message = socket.recv_string()
    print("msg: %s " % message)

    time.sleep(1)

    socket.send(b"world")