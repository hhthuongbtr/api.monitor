import pika

class RabbitMQQueue:
    def __init__(self):
        self.routing_key = 'hello'
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(queue=self.routing_key)

    def get_current_query(self):
        queue_len = self.queue.method.message_count
        if not queue_len:
            #close BlockingConnection
            self.connection.close()
            return ""
        query = ""
        for i in range(queue_len):
            method_frame, header_frame, body = self.channel.basic_get(self.routing_key)
            if method_frame:
                query = query + body
                #clear messages from queue
                self.channel.basic_ack(method_frame.delivery_tag)
            else:
                print 'No message returned'
        #close BlockingConnection
        self.connection.close()
        return query

    def push_query(self,message):
        self.channel.basic_publish(exchange='',
                      routing_key=self.routing_key,
                      body=message,
                      properties=pika.BasicProperties(
                      delivery_mode = 2, # make message persistent
                      ))
        self.connection.close()