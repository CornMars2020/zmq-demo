const zmq = require("zeromq");

async function runServer() {
  const s = new zmq.Reply();

  await s.bind("tcp://*:5555");

  for await (const [msg] of s) {
    console.log("Received " + ": [" + msg.toString() + "]");
    await s.send("World");
    // Do some 'work'
  }
}

runServer();
