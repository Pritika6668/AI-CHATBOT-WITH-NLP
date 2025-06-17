import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there, what can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am a CodTech Chatbot created using Python and NLTK."]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing fine. How can I help you?"]
    ],
    [
        r"(.*) your name?",
        ["You can call me CodBot."]
    ],
    [
        r"(.) help (.)",
        ["Sure! I can help you. Please tell me more about your issue."]
    ],
    [
        r"bye|exit",
        ["Goodbye! Have a great day."]
    ]
]

def codtech_chatbot():
    print("CodTech NLP Chatbot: Hello! Type 'bye' or 'exit' to quit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    codtech_chatbot()