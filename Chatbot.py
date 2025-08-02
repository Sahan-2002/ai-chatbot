from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('SimpleBot')

# Train the chatbot with English data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Chat loop
print("Hello! I'm your chatbot. Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot.get_response(user_input)
    print("Bot:", response)
