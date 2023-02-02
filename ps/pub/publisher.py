# -*- coding: utf-8 -*-

import zmq
import sys
from flask import (request, Flask)

port = "5555"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

app = Flask(__name__)
context = zmq.Context()
socket = context.socket(zmq.PUB)

@app.route('/', methods={"POST"})
def hello():
  if request.method == 'POST':
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
      message = request.json
      socket.send("pubsub %s" % (message))
    return 'Sent to the subscriber/worker.'

if __name__ == "__main__":
  socket.bind("tcp://127.0.0.1:%s" % port)
  app.run(debug=True, port=3000)
