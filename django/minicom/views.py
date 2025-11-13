from django.shortcuts import render
from django.http import JsonResponse
from minicom.models import Conversation, Message

# Customer chat interface view
def chat_view(request, customer_id):
    """
    Renders the chat interface for a customer.
    Each customer gets their own conversation tracked by customer_id.
    """
    return render(request, 'chat.html', {'customer_id': customer_id})

# API to get conversation history (REST endpoint)
def get_conversation(request, customer_id):
    """
    Returns all messages for a customer's conversation as JSON.
    Used for loading chat history.
    """
    try:
        conversation = Conversation.objects.get(customer_id=customer_id)
        messages = Message.objects.filter(conversation=conversation)
        data = {
            'customer_id': customer_id,
            'messages': [{'sender': m.sender, 'content': m.content, 'timestamp': str(m.timestamp)} for m in messages]
        }
        return JsonResponse(data)
    except Conversation.DoesNotExist:
        return JsonResponse({'customer_id': customer_id, 'messages': []})

# Agent dashboard view (HTML)
def agent_dashboard_view(request):
    """
    Dashboard page for agents to see all active conversations.
    """
    return render(request, 'agent_dashboard.html')

# Agent chat interface (HTML)
def agent_chat_view(request, customer_id):
    """
    Agent interface to chat with a specific customer.
    Agent can take over from bot and respond directly.
    """
    return render(request, 'agent_chat.html', {'customer_id': customer_id})

# API: Get all conversations for agent dashboard
def agent_dashboard_api(request):
    """
    API endpoint that returns all conversations as JSON.
    Used by agent dashboard to display conversation list.
    """
    conversations = Conversation.objects.all().order_by('-created_at')
    data = [{
        'customer_id': c.customer_id,
        'is_bot_active': c.is_bot_active,
        'created_at': str(c.created_at),
        'message_count': c.messages.count()
    } for c in conversations]
    return JsonResponse({'conversations': data})

# API: Agent takes over conversation (disables bot)
def agent_takeover(request, customer_id):
    """
    When agent clicks "Take Over", disable bot for this conversation.
    From this point, only human agent responds (no bot).
    """
    try:
        conversation = Conversation.objects.get(customer_id=customer_id)
        conversation.is_bot_active = False
        conversation.save()
        return JsonResponse({'success': True, 'message': 'Agent took over the chat'})
    except Conversation.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Conversation not found'}, status=404)
