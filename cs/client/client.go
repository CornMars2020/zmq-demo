package main

import (
	"fmt"
	"time"

	zmq "github.com/pebbe/zmq4"
)

func main() {
	zctx, _ := zmq.NewContext()

	fmt.Printf("Connecting to the server…\n")
	s, _ := zctx.NewSocket(zmq.REQ)
	s.Connect("tcp://localhost:5555")

	// Do 10 requests, waiting each time for a response
	for i := 0; i < 10; i++ {
		fmt.Printf("Sending request %d…\n", i)
		s.Send("Hello", 0)

		time.Sleep(time.Second * 5)

		result, err := s.Recv(0)
		if err != nil {
			fmt.Printf("recv error %s\n", err)
		}

		fmt.Printf("Received %s\n", result)
	}
}
