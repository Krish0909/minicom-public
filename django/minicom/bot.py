# Simple rule-based chatbot for customer support
# No external dependencies needed - lightweight and fast

def get_bot_response(user_message):
    """
    Generate a simple bot response to customer messages.
    Uses rule-based keyword matching for common support queries.
    In production, replace with ML model or integrate with support platform.
    """

    user_lower = user_message.lower()

    # Greeting detection
    if any(word in user_lower for word in ['hello', 'hi', 'hey', 'good morning', 'good afternoon']):
        return "Hi there! 👋 I'm your support bot. How can I help you today?"

    # Help/support requests
    if any(word in user_lower for word in ['help', 'support', 'assist']):
        return "I'd be happy to help! Could you describe your issue in detail? A human agent can also join if needed."

    # Problem/issue keywords
    if any(word in user_lower for word in ['problem', 'issue', 'error', 'bug', 'broken', 'not working']):
        return "I'm sorry you're experiencing an issue. Can you tell me more about what's happening? When did this start?"

    # Account-related
    if any(word in user_lower for word in ['account', 'login', 'password', 'sign in']):
        return "For account issues, I can help! Are you having trouble logging in, or do you need to reset your password?"

    # Billing/payment
    if any(word in user_lower for word in ['billing', 'payment', 'charge', 'invoice', 'subscription']):
        return "I can help with billing questions. Let me connect you with our billing team for accurate information."

    # Thanks/gratitude
    if any(word in user_lower for word in ['thanks', 'thank you', 'appreciate']):
        return "You're very welcome! Is there anything else I can help you with? 😊"

    # Bye/ending
    if any(word in user_lower for word in ['bye', 'goodbye', 'see you', 'later']):
        return "Goodbye! Feel free to reach out anytime you need assistance. Have a great day!"

    # Question detection
    if '?' in user_message:
        return "That's a great question! Let me help you with that. Can you provide a bit more context?"

    # Default response for anything else
    return "Thanks for reaching out! I'm processing your message. Could you provide more details so I can better assist you?"
