package main

import (
	"fmt"

	zmq "github.com/pebbe/zmq4"
)

func main() {
	zctx, _ := zmq.NewContext()

	fmt.Printf("Connecting to server…\n")
	s, _ := zctx.NewSocket(zmq.SUB)
	s.Connect("tcp://localhost:5555")
	s.SetSubscribe("pubsub")

	for {
		topic, err := s.Recv(0)
		if err != nil {
			continue
		}

		if msg, err := s.Recv(0); err == nil {
			fmt.Printf("Received from channel: %s\n", topic)
			fmt.Println(msg)
		}
	}
}
