import pyttsx3
import random

# https://memesbams.com/cheer-up-quotes/
pos_sentences = ["Life is a mixture of sunshine and rain, teardrops and laughter, pleasure and pain. Just remember, there was never a cloud that the sun couldn’t shine through.",
    "God gives us dreams at night so that we can turn them into reality during the day. So have faith and move ahead.",
    "Good people are good because they’ve come to wisdom through failure.",
    
    "Life is a mixture of sunshine and rain, teardrops and laughter, pleasure and pain. Just remember, there was never a cloud that the sun couldn’t shine through.",
    "God gives us dreams at night so that we can turn them into reality during the day. So have faith and move ahead.",
    "Good people are good because they’ve come to wisdom through failure.",

 ]

# https://christinarebuffet.com/blog/how-to-complain-politely-in-english/
neg_sentences = ["Excuse me, I know this isn’t your fault, but I ordered my steak well-done, and it’s not cooked enough.",
    "Sorry to bother you, but I’d like to make a complaint about a rude employee. I asked 3 times for some help, he looked at me, and just walked away",
    "How can we fix this?",

    ]

all_sentences = pos_sentences + neg_sentences

msg = random.choice(all_sentences)

engine = pyttsx3.init()

# talking speed
rate = engine.getProperty('rate') # getting details of current speaking rate
print (rate) #printing current voice rate
engine.setProperty('rate', 190) # setting up new voice rate

# gender
MALE = 0
FEMALE = 1
n = random.choice([MALE, FEMALE])
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[n].id)

# speak
print(msg)
engine.say(msg)
engine.runAndWait()