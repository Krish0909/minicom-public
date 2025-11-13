# 🚀 Quick Start Guide

## Server is Running!

Your Minicom customer support system is live at **http://localhost:8000**

---

## 🎯 Three Simple Steps to Demo

### 1. Customer Chat (Window 1)
Open: **`http://localhost:8000/chat/alice/`**
- Type a message
- Bot responds automatically

### 2. Agent Dashboard (Window 2)
Open: **`http://localhost:8000/agent/dashboard/`**
- See all conversations
- Click on "alice" to join

### 3. Agent Takes Over (Same Window 2)
- View conversation history
- Click "Take Over Chat"
- Reply to customer
- Bot stops responding

---

## 📍 All URLs

### Customer Interface
```
http://localhost:8000/chat/alice/
http://localhost:8000/chat/bob/
http://localhost:8000/chat/[any-customer-id]/
```

### Agent Interface
```
http://localhost:8000/agent/dashboard/      ← START HERE
http://localhost:8000/agent/chat/alice/
```

---

## ✨ What You Built

✅ **Real-time WebSocket chat** (low latency)
✅ **AI bot** responds automatically (rule-based)
✅ **Human agent takeover** - bot stops when agent joins
✅ **Conversation persistence** - SQLite database
✅ **Multi-customer support** - each has own thread
✅ **Agent dashboard** - view all active chats
✅ **Three-way messaging** - customer ↔ bot ↔ agent

---

## 🎬 Quick Demo Flow

1. Open customer window: `http://localhost:8000/chat/alice/`
2. Open agent dashboard: `http://localhost:8000/agent/dashboard/`
3. Customer types: "Hello, I need help"
4. Bot responds automatically
5. Agent clicks on "alice" conversation
6. Agent clicks "Take Over Chat"
7. Agent types a reply
8. Customer sees agent message instantly!
9. Bot no longer responds

---

## 📖 Read More

- `DEMO_GUIDE.md` - Detailed demo script for interview
- `IMPLEMENTATION_README.md` - Technical architecture details

---

## 🛠️ To Restart Server

```bash
# Kill server (if needed)
pkill -f daphne

# Start server
venv/bin/daphne -b 0.0.0.0 -p 8000 minicom.asgi:application
```

---

## 🎯 Key Points for Interview

1. **WebSocket = Real-time** - No polling, instant updates
2. **Bot handoff** - Smart transition from bot to human
3. **Persistence** - All messages saved to database
4. **Scalable pattern** - Clean separation of concerns
5. **Minimal code** - Production-ready patterns, no bloat

Good luck with your interview! 🚀
