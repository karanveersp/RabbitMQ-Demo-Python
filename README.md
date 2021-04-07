# Python RabbitMQ Demo

## Starting RabbitMQ

You can start a RabbitMQ server in Docker using

`docker run -it --rm -p 5672:5672 -p 15672:15672 rabbitmq:3-management`

Visit `http://localhost:15672` to see the RabbitMQ manager webpage.

## Running the demo

Start the receiver

`python receive.py`


Then run the send in another terminal window

`python send.py`

You'll see the data appear in the receive terminal window.