# -*- coding: utf-8 -*-

import sys
import zmq

port = "5555"
if len(sys.argv) > 1:
  port =  sys.argv[1]
  int(port)

context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Connecting to server…")
socket.connect ("tcp://localhost:%s" % port)

topic = "pubsub"
socket.setsockopt_string(zmq.SUBSCRIBE, topic)

while True:
  topic = socket.recv()
  message = socket.recv()
  
  print("Received from channel %s:", topic)
  print(message)
