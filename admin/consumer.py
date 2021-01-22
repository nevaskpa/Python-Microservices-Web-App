import pika

params = pika.URLParameters(
    "amqps://wlvrwvtf:1OjaaWuYLgy_2BLdzIxP6oMdCTED4SDX@shrimp.rmq.cloudamqp.com/wlvrwvtf")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Receiving message in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()
channel.close()