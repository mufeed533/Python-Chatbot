"""
Author : Muhammed Mufeed K
mufeedm533@gmail.com
Main file for chat bot application. Components present in this code are :   1) train the chat bot (refer train section for more details)
2) get data from the user
3) process the user input, find the best match from the trained instances aand return the best matched output.
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


chatbot = ChatBot("bot")    # create an instance of ChatBot and name it. We can add additional paramters here. Refer ChatterBot official doc for further details.
chatbot.set_trainer(ListTrainer)
"""
Get the data files for training. I used English conversation for training the bot.
"""
root_directory = os.path.dirname(__file__)
file_name = os.path.join(root_directory,"chatterbot-corpus-master/chatterbot_corpus/data/english")
for file in os.listdir(file_name):
    data = open(file_name+"/"+file , "r").readlines()
    chatbot.train(data)   # train the bot using the data collected
"""
Question and answer part. Here we get input from user and process it using teh chat bot instance. Send the response back to the terminal.
"""
while True:
    try:
        user_input = input("you - ")
        bot_input = chatbot.get_response(user_input)
        print("bot - ",bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
