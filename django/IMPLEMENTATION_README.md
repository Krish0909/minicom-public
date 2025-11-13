# Minicom - Customer Support Chat Application

A minimal customer support chat application built with Django Channels and WebSockets for real-time messaging.

## Architecture

This is a **customer support application** with:

1. **One-to-One Conversations**: Each customer has their own conversation thread
2. **Real-time WebSocket Communication**: Low-latency messaging using Django Channels
3. **AI Bot Assistant**: Simple HuggingFace-based bot responds until human agent takes over
4. **Message Persistence**: All conversations stored in SQLite database

## Key Components

### Backend (Django)

- `models.py`: Conversation and Message models for DB persistence
- `consumers.py`: WebSocket consumer handling real-time chat with async/await
- `bot.py`: Simple AI bot using HuggingFace distilgpt2 (no API key needed)
- `views.py`: Customer chat interface and API endpoints
- `asgi.py`: ASGI configuration for WebSocket routing

### Frontend (Vanilla JS)

- `templates/chat.html`: Clean customer chat interface with WebSocket connection

### How It Works

1. **Customer opens chat** → `/chat/<customer_id>/`
2. **WebSocket connects** → Loads message history from DB
3. **Customer sends message** → Saved to DB, broadcast via WebSocket
4. **Bot responds** → If `is_bot_active=True`, bot generates response
5. **Agent can take over** → Set `is_bot_active=False` to disable bot

## Setup & Installation

### Quick Start

```bash
# Run the setup script
./setup.sh
```

### Manual Setup

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations minicom
python manage.py migrate

# Start the WebSocket server (use daphne, not runserver)
daphne -b 0.0.0.0 -p 8000 minicom.asgi:application
```

## Testing

### Two-Window Demo

1. Open browser window 1: `http://localhost:8000/chat/customer1/`
2. Open browser window 2: `http://localhost:8000/chat/customer1/`
3. Type in either window - messages appear in real-time in both
4. Bot responds automatically to customer messages

### Different Customers

- Window 1: `http://localhost:8000/chat/alice/`
- Window 2: `http://localhost:8000/chat/bob/`
- Each has separate conversation history

## API Endpoints

- `GET /api/conversation/<customer_id>/` - Get conversation history (JSON)
- `GET /api/agent/dashboard/` - View all active conversations
- `WS /ws/chat/<customer_id>/` - WebSocket endpoint for real-time chat

## Code Structure

### WebSocket Flow (consumers.py)

```
connect() → Get/create conversation → Send message history
receive() → Save customer message → Broadcast to group → Generate bot response
```

### Bot Logic (bot.py)

- Rule-based responses for common phrases (hello, help, thanks)
- Falls back to HuggingFace distilgpt2 for natural responses
- Lightweight, runs without API keys

### Database Schema

```
Conversation:
  - customer_id (unique identifier)
  - is_bot_active (bot on/off switch)
  - created_at

Message:
  - conversation (FK)
  - sender (customer/bot/agent)
  - content
  - timestamp
```

## Key Features Demonstrated

✅ Real-time WebSocket messaging (low latency)
✅ Conversation history persistence in SQLite
✅ AI bot integration (HuggingFace, no API key)
✅ Clean separation: customer view vs agent view
✅ Minimal code, production patterns
✅ Async/await for WebSocket handling

## Interview Tips

- **Think out loud**: Explain your thought process
- **Understand the code**: Every line has a purpose
- **Be collaborative**: Discuss trade-offs and alternatives
- **Ask questions**: Clarify requirements before coding

## Time Spent

This implementation was designed to be completed in **45 minutes**:
- Models & DB setup: 5 min
- WebSocket consumer: 15 min
- Bot integration: 10 min
- Frontend interface: 10 min
- Testing & refinement: 5 min
