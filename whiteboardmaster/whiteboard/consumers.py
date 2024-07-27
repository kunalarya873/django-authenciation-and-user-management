from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.board_room = 'board_room'
        await self.channel_layer.group_add(
            self.board_room,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.board_room,
            self.channel_name
        )
        print("disconnected", close_code)

    async def receive(self, text_data):
        initial_data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.board_room,
            {
                "type": "board_message",
                "text": json.dumps(initial_data)
            }
        )
        print("receive", initial_data)
        
    async def board_message(self, event):
        await self.send(text_data=event["text"])
