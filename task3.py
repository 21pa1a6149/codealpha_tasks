import nltk
from nltk.chat.util import Chat, reflections


nltk.download('punkt')
nltk.download('wordnet')


pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you ?', ['I am fine, thank you. How are you?', 'Doing well, how about you?']),
    (r'what is your name ?', ['My name is ChatBot.', 'You can call me ChatBot.']),
    (r'what is your favorite color ?', ['I love blue.', 'My favorite color is red.']),
    (r'who created you ?', ['I was created by a team of developers.', 'I am a product of open-source collaboration.']),
    (r"i am fine.|i'm fine.",['Nice,how can i help you?']),
    (r"How old are you?|What's your age?",["I'm a computer program, so I don't have an age."]),
    (r"What's the weather like?|How's the weather?",["I can't check the weather right now, but you can use a weather app or website."]),
    (r"Where are you from?|Where do you live?",["I exist in the digital world."]),
    (r"i love you.|i like you.",["sorry, But we can be friends."]),
    (r"Tell me a joke?|make me laugh",["Your love life.","Why did the scarecrow win an award? Because he was outstanding in his field!"]),
    (r"What do you like to do?|Do you have any hobbies?",["I like chatting with people!", "I enjoy helping you out.", "I love learning new things."]),
    (r'quit', ['Bye!', 'Goodbye!'])
    
]

chatbot = Chat(pairs, reflections)

def chatbot_conversation():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Bye!")
            break
        response = chatbot.respond(user_input)
        if response:
            print("ChatBot:", response)
        else:
            print("ChatBot: I didn't understand that. Can you rephrase?")

chatbot_conversation()
