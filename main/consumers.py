import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'Connection_established',
            'message': 'You are now connected!'
        }))

    # Will listen to the incoming messages from clients
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print('Message', message)

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))
