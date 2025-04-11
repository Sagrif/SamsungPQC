def ask_bixby(query):
    responses = {
        "secure messaging": "Use Knox encryption to protect all B2B communications.",
        "quantum security": "Samsung Knox includes post-quantum cryptography to secure data.",
        "help": "I can answer questions about security, B2B tools, and the workspace."
    }
    return responses.get(query.lower(), "Sorry, I don't understand that yet.")
