const Fast = require("fastify");
const zmq = require("zeromq");

const app = new Fast();
const p = new zmq.Publisher();

app.post("/", async (request, reply) => {
  const msg = JSON.stringify({ ...request.body });
  console.log("Received: %s", msg);

  await p.send(["pubsub", msg]);
  return reply.send("Sent to the subscriber/worker.");
});

const main = async () => {
  try {
    await p.bind("tcp://*:5555");
    await app.listen({ port: 3000 });
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
};
main();
