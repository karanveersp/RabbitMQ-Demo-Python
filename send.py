"""
Sends a single message to the queue and exits.
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

channel.queue_declare("hello")

channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")

print("Sent 'Hello World!'")


connection.close()  # flushes network buffers and gently closes connection.