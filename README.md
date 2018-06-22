A chat bot powered by machine learning algorithms. Core engine is developed with the help of ChatterBot module from Python.

Features:

1) The bot can answer casual questions.

you - hai
bot -  what is your name?
you - mufeed
bot -  How are you doing?
you - i am fine
bot -  That is good to hear.

2) can detect emotions.

you - you are jealous
bot -  - Normally, as a bot i don't have feelings.
you - you are never nice
bot -  - I try to be as nice as I can.
you - you should be ashamed
bot -  - Shame is a common human emotion.

Note : The bot works on the basis of data you provide. So please don't expect miracle from it.

3) The bot can be trained to with custom data to make it more intelligent.
  How to add your own data?
  - feed your question and answers to a yaml file.(refer chatterbot_corpus direcotry for examples)
  - add the data file location to the training section in chat-bot.py
  - run the code. you can see the model gets trained.
   List Trainer: [####################] 100%
   List Trainer: [####################] 100%
   List Trainer: [####################] 100%

   Note : Each time you run the chat-bot.py the bot will be trained. To avoid that comment out the training part after first train.

Usage

1. clone or the repository
2. Install all the libraries specified in requirements.txt
3. Go to the main directory using command line and execute 'python3 chat-bot.py'
4. Type your questions in the command line once the training has been completed.
5. press ctrl+z or ctrl+c to exit the program

Note : Tested only in Centos 7
