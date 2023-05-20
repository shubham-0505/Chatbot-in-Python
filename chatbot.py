import nltk
import random

from nltk.chat.util import Chat, reflections

pattern = [(r"Hello|Hi|Hey",["Hi! What can I do for you?"]),
(r"What is your name?",["My name is Virtual Assistant. What's yours?"]),
(r"My name is (.*)",["Hello %1,How can I help you?"]),
(r"What can you do?",["I can help you with variety of tasks like writing an essay,checking errors in code and lot more !"]),
(r"Ok Bye",["Have a nice day !"])]

# Creating a chatbot
chatbot = Chat(pattern,reflections)

# Initializing chatbot	
print("Hey there! How may I help?")
chatbot.converse()
