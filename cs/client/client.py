# -*- coding: utf-8 -*-

import zmq
import sys

port = "5555"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()

print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)

for i in range (1,10):
    print("Sending Hello ", i)
    socket.send_string("Hello")
    
    message = socket.recv()
    print("Received ", message, i)