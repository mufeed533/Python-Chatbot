from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("bot")
conversation = [
"Hello",
"Hai there !",
"How are you doing?",
"I am doing great !",
"That is good to hear.",
"Thank you",
"You are welcome"
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

user_input = input()
response = chatbot.get_response("user_input")
print(response)
