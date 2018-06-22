from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

chatbot = ChatBot("bot")
chatbot.set_trainer(ListTrainer)

root_directory = os.path.dirname(__file__)
file_name = os.path.join(root_directory,"chatterbot-corpus-master/chatterbot_corpus/data/english")
for file in os.listdir(file_name):
    data = open(file_name+"/"+file , "r").readlines()
    chatbot.train(data)

while True:
    try:
        user_input = input("you - ")
        bot_input = chatbot.get_response(user_input)
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
