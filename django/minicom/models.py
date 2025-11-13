from django.db import models

# Represents a conversation between a customer and support
class Conversation(models.Model):
    customer_id = models.CharField(max_length=100)  # Simple customer identifier
    created_at = models.DateTimeField(auto_now_add=True)
    is_bot_active = models.BooleanField(default=True)  # True = bot responds, False = human took over

    class Meta:
        db_table = 'conversations'

# Individual messages within a conversation
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=20)  # 'customer', 'bot', or 'agent'
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messages'
        ordering = ['timestamp']
