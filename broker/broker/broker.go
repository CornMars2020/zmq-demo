package main

import (
	"log"

	zmq "github.com/pebbe/zmq4"
)

func main() {
	zctx, err := zmq.NewContext()
	if err != nil {
		log.Fatal(err)
	}

	p, err := zctx.NewSocket(zmq.XPUB)
	if err != nil {
		log.Fatal(err)
	}
	p.Bind("tcp://*:5555")

	s, err := zctx.NewSocket(zmq.XSUB)
	if err != nil {
		log.Fatal(err)
	}
	s.Bind("tcp://*:5554")

	zmq.Proxy(p, s, nil)
}
