const zmq = require("zeromq");
const { sleep } = require("../../../../libs/utils/sleep");

async function runClient() {
  console.log("Connecting to server…");

  const sock = new zmq.Request();
  sock.connect("tcp://localhost:5555");

  for (let i = 0; i < 10; i++) {
    console.log("Sending Hello ", i);
    await sock.send("Hello");

    await sleep(2000);

    const [result] = await sock.receive();
    console.log("Received ", result.toString(), i);
  }
}

runClient();