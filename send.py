"""
Sends messages entered by the user to the queue.
"""

import pika

def main():
    
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    channel = connection.channel()

    channel.queue_declare("hello")

    try:
        while True:
            print()
            message = input("> ")
            channel.basic_publish(exchange="", routing_key="hello", body=message)
            print(f"Sent '{message}'")
    except KeyboardInterrupt:
        print("Exiting")
        connection.close()
        exit(0)


if __name__ == "__main__":
    main()