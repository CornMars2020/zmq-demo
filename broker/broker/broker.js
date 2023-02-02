const zmq = require("zeromq");

async function runBroker() {
  const p = new zmq.XPublisher();
  await p.bind("tcp://*:5555");

  const s = new zmq.XSubscriber();
  await s.bind("tcp://*:5554");

  const proxy = new zmq.Proxy(p, s);
  await proxy.run();
}

runBroker();
