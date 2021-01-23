import pika, json

params = pika.URLParameters(
    "amqps://wlvrwvtf:1OjaaWuYLgy_2BLdzIxP6oMdCTED4SDX@shrimp.rmq.cloudamqp.com/wlvrwvtf")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
