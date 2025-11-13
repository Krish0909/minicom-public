# Minicom Demo Guide - Complete Workflow

## Overview
You now have a **full customer support chat system** with:
- Customer interface (chats with bot)
- Agent dashboard (views all conversations)
- Agent chat interface (human takeover from bot)
- Real-time WebSocket messaging

---

## 🎯 Complete Demo Workflow

### Step 1: Customer Starts Chat
1. Open browser window: `http://localhost:8000/chat/alice/`
2. Customer "alice" sees empty chat
3. Type: "Hello, I need help"
4. **Bot responds automatically** with greeting

### Step 2: Agent Views Dashboard
1. Open new browser window: `http://localhost:8000/agent/dashboard/`
2. See list of active conversations
3. Notice "alice" conversation with **🤖 BOT** badge
4. Shows message count and timestamp

### Step 3: Agent Takes Over
1. Click on "alice" conversation in dashboard
2. Opens agent chat interface: `http://localhost:8000/agent/chat/alice/`
3. See full conversation history (customer + bot messages)
4. Click **"Take Over Chat"** button
5. Status changes to **👤 Human Agent**
6. Input field becomes enabled

### Step 4: Real-time Agent Response
1. In agent window, type: "Hi Alice, I'm a human agent. How can I help?"
2. Press Send
3. **Switch to customer window** - see agent message appear instantly!
4. Bot no longer responds (human has taken over)

### Step 5: Two-way Conversation
1. **Customer window**: Type "I have a billing question"
2. **Agent window**: See customer message appear in real-time
3. **Agent window**: Reply "Let me check your account..."
4. **Customer window**: See agent response instantly
5. All messages saved to database

---

## 🔥 Quick Demo URLs

### Customer Interface
- `http://localhost:8000/chat/alice/` - Customer "alice"
- `http://localhost:8000/chat/bob/` - Customer "bob"
- `http://localhost:8000/chat/customer123/` - Any customer ID

### Agent Interface
- `http://localhost:8000/agent/dashboard/` - **START HERE** (agent dashboard)
- Shows all active conversations
- Click any conversation to join

### API Endpoints (JSON)
- `http://localhost:8000/api/agent/dashboard/` - All conversations (JSON)
- `http://localhost:8000/api/conversation/alice/` - Alice's messages (JSON)

---

## 💡 Key Features to Highlight

### 1. Real-time WebSocket Communication
- Open customer window and agent window side by side
- Type in either - messages appear instantly in both
- **Zero refresh needed** - pure real-time

### 2. Smart Bot Handoff
- Bot responds automatically when customer sends message
- Agent clicks "Take Over" → bot stops responding
- Agent messages appear as "🎧 Agent" (green)
- Bot messages appear as "🤖 Bot" (orange)
- Customer messages appear as "👤 Customer" (blue)

### 3. Conversation Persistence
- All messages saved to SQLite database
- Close browser and reopen - history loads automatically
- Each customer has their own conversation thread

### 4. Multi-conversation Support
- Agent dashboard shows ALL active conversations
- Each customer (alice, bob, etc.) has separate thread
- Agent can jump between conversations

---

## 🎬 Interview Demo Script

**"Let me show you the customer support flow:"**

1. **Customer View** (Window 1):
   - "Here's what a customer sees when they start a chat"
   - Type: "Hi, I need help with my account"
   - "Notice the bot responds immediately"

2. **Agent Dashboard** (Window 2):
   - "Meanwhile, our support agents see this dashboard"
   - "They can see all active conversations and their status"
   - "Let me click on this customer's conversation"

3. **Agent Chat** (Same Window 2):
   - "Now I'm viewing the full conversation history"
   - "I can see the customer chatting with the bot"
   - "Let me take over this conversation" *[click button]*

4. **Agent Responds** (Window 2):
   - Type: "Hi! I'm a human agent, I can help you with that."
   - "Watch the customer window..."

5. **Customer Sees Agent** (Window 1):
   - "The message appears instantly!"
   - "And notice - the bot has stopped responding"
   - "Now it's a direct human conversation"

6. **Two-way Chat**:
   - Demonstrate back-and-forth messaging
   - Show real-time updates in both windows
   - Explain all messages are persisted to database

---

## 🏗️ Architecture Highlights

### WebSocket Flow
```
Customer sends message
    ↓
WebSocket → Django Channels Consumer
    ↓
Save to SQLite database
    ↓
Broadcast to all connected clients (customer + agent)
    ↓
If bot_active: Generate bot response → Broadcast again
```

### Human Takeover
```
Agent clicks "Take Over"
    ↓
POST to /api/agent/takeover/
    ↓
Set conversation.is_bot_active = False
    ↓
Bot stops responding
    ↓
Only agent messages sent
```

### Database Schema
```
Conversation:
  - customer_id (unique identifier)
  - is_bot_active (True/False switch)
  - created_at

Message:
  - conversation (FK)
  - sender (customer/bot/agent)
  - content
  - timestamp
```

---

## 🧪 Testing Checklist

- [ ] Customer can send messages
- [ ] Bot responds automatically
- [ ] Agent dashboard shows conversations
- [ ] Agent can view conversation history
- [ ] Agent can take over from bot
- [ ] Agent messages appear in customer window
- [ ] Customer messages appear in agent window
- [ ] Bot stops responding after takeover
- [ ] Multiple customers have separate conversations
- [ ] Messages persist after page refresh

---

## 📂 Key Files

- `minicom/models.py` - Database models (Conversation, Message)
- `minicom/consumers.py` - WebSocket handler (real-time messaging)
- `minicom/bot.py` - Rule-based bot responses
- `minicom/views.py` - Customer and agent views
- `templates/chat.html` - Customer interface
- `templates/agent_dashboard.html` - Agent conversation list
- `templates/agent_chat.html` - Agent chat interface

---

## 🎯 Interview Tips

1. **Explain as you code**: "I'm using Django Channels for WebSocket support..."
2. **Think out loud**: "The agent needs to see conversation history, so..."
3. **Show trade-offs**: "I used rule-based bot for simplicity, but could integrate OpenAI..."
4. **Be collaborative**: "What do you think about this approach?"
5. **Demonstrate**: Open 2-3 browser windows and show live messaging

---

## 🚀 Production Considerations

**Things you can mention (but didn't implement):**
- Redis for channel layers (instead of in-memory)
- PostgreSQL for production database
- ML-based bot (Dialogflow, Rasa, or OpenAI)
- Authentication for agents
- Message read receipts
- Typing indicators
- File attachments
- Agent assignment logic
- Conversation routing
- Analytics and metrics
