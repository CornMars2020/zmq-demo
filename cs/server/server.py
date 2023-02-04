# -*- coding: utf-8 -*-

import zmq
import time
import sys

port = "5555"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
s = context.socket(zmq.REP)
s.bind("tcp://*:%s" % port)

while True:
  message = s.recv()
  print("Received request: ", message)
  time.sleep(1)
  s.send("World from %s" % port)
