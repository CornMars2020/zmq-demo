package main

import (
	"github.com/gofiber/fiber/v2"
	zmq "github.com/pebbe/zmq4"
)

func main() {
	app := fiber.New()
	zctx, _ := zmq.NewContext()

	p, _ := zctx.NewSocket(zmq.PUB)
	p.Bind("tcp://*:5555")

	app.Post("/", func(c *fiber.Ctx) error {
		p.Send("pubsub", zmq.SNDMORE)
		p.Send(string(c.Body()), 0)
		return c.SendString("Sent to the subscriber/worker.")
	})

	app.Listen(":3000")

}
