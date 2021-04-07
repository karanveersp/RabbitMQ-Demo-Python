import sys
import os
import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare("hello")  # idempotent, will return existing, or create if not exists

    # good practice to repeat queue declaration in both sender and receiver

    def callback(ch, method, properties, body):
        print(f"Received {body}")

    # tell RabbitMQ that this callback should receive messages from the 'hello' queue

    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

    print("Waiting for messages. To exit press CTRL-C")

    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemError:
            os._exit(0)
