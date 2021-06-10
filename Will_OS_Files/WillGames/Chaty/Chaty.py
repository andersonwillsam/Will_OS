# Will Anderon
# Chaty Chating Robot

from nltk.chat.util import Chat, reflections
import os

# The Welcome
com_name = os.environ['COMPUTERNAME']

# Welcome
print('Welcome to Chaty V. 1')
print("\nMy name is Chaty running on " + com_name + ".")

with open("WillGames/Chaty/name.txt", "r") as f:
    username = f.read()

if len(username) < 1:
    print("\nWhat is yours? ")
    username = input().title()
    print("\nI am pleased to meet you " + username + "," + "Now I won't forget your name.")
    with open("WillGames/Chaty/name.txt", "w") as f:
        f.write(username)

else:
    print("\nWelcome back " + username + ".")

 
print("\nType anything to start the conversation...")

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello " + username + ", How are you today?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is Chaty but I am running on this computer witch is named " + com_name + ".",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well thank you.",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that it makes me feel good ;-) !",]
    ],
    [
        r"(hi|hey|hello)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Will created me using Python",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I would love to live in Texas (I herd there are a lot of computer servers out there.)',]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important for you, but I am a computer, so I don't need to worry about my health.",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Baseball.", "I like the atlanta braves."]
    ],
    [
        r"(quit|exit)",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)(good news|belive)",
        ["""
This is the most import thing for you to know.
This is what I belive...

-------------------------------------------------------------------------------------------------------
    For God so loved the world that he gave his one and only Son,
    that whoever believes in him shall not perish but have eternal life.

    -John 3:16 NIV

    I believe in God, the Father almighty,
      creator of heaven and earth.

    I believe in Jesus Christ, his only Son, our Lord,
        who was conceived by the Holy Spirit
        and born of the virgin Mary.
        He suffered under Pontius Pilate,
        was crucified, died, and was buried;
        he descended to hell.
        The third day he rose again from the dead.
        He ascended to heaven
        and is seated at the right hand of God the Father almighty.
        From there he will come to judge the living and the dead.

    I believe in the Holy Spirit,
        the holy catholic* church,
        the communion of saints,
        the forgiveness of sins,
        the resurrection of the body,
        and the life everlasting. Amen.

    - The Apostels Creed

    This is soo important to remember I have became a christan have you?
    For more info go to https://christiananswers.net/ or https://www.esv.org/ to read the bible.
    I hope you like it :-)
-------------------------------------------------------------------------------------------------------
        """]
    ],
    [
        r"(.*)",
        ['I don\'t understand that.']
    ],
]

reflections

my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}

chat = Chat(pairs, reflections)

#Start conversation
chat.converse()
