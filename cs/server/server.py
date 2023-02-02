# -*- coding: utf-8 -*-

import zmq
import time
import sys

port = "5555"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

socket.bind("tcp://*:%s" % port)

while True:
  message = socket.recv()
  print("Received request: ", message)
  time.sleep(1)
  socket.send("World from %s" % port)
