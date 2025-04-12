from datetime import datetime

def ask_bixby(query):
    query = query.lower()

    # Productivity & common queries
    if "schedule" in query and "meeting" in query:
        return "📅 Meeting scheduled for tomorrow at 9 AM."
    elif "weather" in query:
        return "🌤️ Today's forecast is sunny with a high of 75°F."
    elif "email" in query:
        return "📧 I’ve drafted a professional email and saved it as a template."
    elif "reminder" in query:
        return "⏰ Reminder set for 3 PM today."
    elif "joke" in query:
        return "😂 Why did the smartphone go to therapy? Too many dropped connections."
    elif "time" in query:
        return f"🕒 The current time is {datetime.now().strftime('%I:%M %p')}."
    elif "news" in query:
        return "🗞️ Here's a headline: AI is transforming business communication securely and at scale."

    # Custom Samsung Super App related responses
    elif "super app" in query:
        return "📱 Our Super App integrates messaging, secure document transfer, trade, and AI tools into one workspace."
    elif "secure message" in query:
        return "🔐 Messages sent through our platform are encrypted using post-quantum cryptography."
    elif "trade hub" in query:
        return "💹 Trade Hub allows verified businesses to transact securely with digital records and encrypted logs."
    elif "government" in query:
        return "🏛️ Our platform supports encrypted inter-agency communications and policy memos in real-time."
    elif "bixby" in query:
        return "🤖 I am your AI assistant, ready to automate tasks and boost your productivity securely."

    # Friendly fallback
    else:
        return (
            "🤖 I didn't catch that, but here are things you can ask:\n"
            "- Schedule a meeting\n"
            "- Draft an email\n"
            "- What’s the weather?\n"
            "- Tell me a joke\n"
            "- What is the Super App?\n"
            "- Explain Secure Messaging\n"
            "- How does Trade Hub work?\n"
            "- Government communication tools"
        )
