import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from minicom.models import Conversation, Message
from minicom.bot import get_bot_response

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract customer_id from URL route
        self.customer_id = self.scope['url_route']['kwargs']['customer_id']
        self.room_group_name = f'chat_{self.customer_id}'

        # Join room group for real-time updates
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Get or create conversation for this customer
        self.conversation = await self.get_or_create_conversation()

        # Send message history to customer on connect
        messages = await self.get_message_history()
        await self.send(text_data=json.dumps({
            'type': 'history',
            'messages': messages
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming message from customer OR agent
        data = json.loads(text_data)
        message_content = data['message']
        sender = data.get('sender', 'customer')  # Default to customer if not specified

        # Save message to DB
        await self.save_message(sender, message_content)

        # Broadcast to all connected clients (customer + agent views)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender': sender,
                'message': message_content
            }
        )

        # Only trigger bot response if:
        # 1. Message is from customer (not agent)
        # 2. Bot is still active (human hasn't taken over)
        if sender == 'customer' and await self.is_bot_active():
            bot_response = await self.generate_bot_response(message_content)
            await self.save_message('bot', bot_response)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'sender': 'bot',
                    'message': bot_response
                }
            )

    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'message',
            'sender': event['sender'],
            'message': event['message']
        }))

    @database_sync_to_async
    def get_or_create_conversation(self):
        # Get or create conversation for customer
        conv, created = Conversation.objects.get_or_create(
            customer_id=self.customer_id,
            defaults={'is_bot_active': True}
        )
        return conv

    @database_sync_to_async
    def get_message_history(self):
        # Fetch all messages for this conversation
        messages = Message.objects.filter(conversation=self.conversation)
        return [{'sender': m.sender, 'content': m.content} for m in messages]

    @database_sync_to_async
    def save_message(self, sender, content):
        # Save message to database
        Message.objects.create(
            conversation=self.conversation,
            sender=sender,
            content=content
        )

    @database_sync_to_async
    def is_bot_active(self):
        # Check if bot should respond or if human agent took over
        self.conversation.refresh_from_db()
        return self.conversation.is_bot_active

    @database_sync_to_async
    def generate_bot_response(self, user_message):
        # Call the bot AI function
        return get_bot_response(user_message)
