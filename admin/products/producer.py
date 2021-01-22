import pika

params = pika.URLParameters(
    "amqps://wlvrwvtf:1OjaaWuYLgy_2BLdzIxP6oMdCTED4SDX@shrimp.rmq.cloudamqp.com/wlvrwvtf")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='Hello from main')
