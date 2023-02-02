const zmq = require("zeromq");

async function runClient() {
  console.log("Connecting to server…");

  const sock = new zmq.Subscriber();
  sock.connect("tcp://localhost:5555");
  sock.subscribe("pubsub");

  for await (const [topic, msg] of sock) {
    console.log("Received from channel %s:", topic);
    console.log(JSON.parse(msg));
  }
}

runClient();
