import random

responses = {
    "greeting": [
        "Hello! How can I assist you today?",
        "Hey there! What can I help you with?",
        "Hi! Feel free to ask me anything.",
        "Greetings! How’s your day going?",
        "Hey! It's great to see you!",
    ],
    "farewell": [
        "Goodbye! Have a nice day!",
        "See you later! Take care.",
        "Thanks for chatting. Talk to you soon!",
        "Catch you later! Don't hesitate to reach out again.",
        "Goodbye! Stay safe and take care!",
    ],
    "help": [
        "I can assist with [list of services, e.g., answering questions, performing tasks, etc.]. What would you like help with?",
        "If you're unsure what to ask, just let me know, and I'll help guide you.",
        "Need some help? Feel free to ask me anything.",
        "I’m here to help with anything you need. How can I assist you?",
    ],
    "error": [
        "Sorry, I didn’t quite catch that. Could you please rephrase?",
        "Oops! Something went wrong. Let me try that again.",
        "I’m having trouble understanding. Could you say that again in a different way?",
        "I'm not sure what you mean, can you clarify?",
    ],
    "joke": [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "I’m terrible at math, but I know a lot of ways to add value to your day!",
        "What’s orange and sounds like a parrot? A carrot!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "How does a penguin build its house? Igloos it together!",
    ],
    "small_talk": [
        "How are you doing today?",
        "What’s on your mind?",
        "Anything exciting happening today?",
        "Is there something you want to talk about?",
        "What have you been up to recently?",
        "How’s your day been going so far?",
    ],
    "confirmation": [
        "I’ve got everything covered. Let me know if anything else comes up.",
        "I’m all set! Feel free to ask me anything anytime.",
        "I’ve saved your request. You’re good to go!",
        "All done! Anything else I can help with?",
        "Everything’s good to go! Anything else I can do for you?",
    ],
    "gratitude": [
        "You're welcome! Let me know if you need anything else.",
        "Glad to be of help! Anything else on your mind?",
        "No problem at all! I'm happy to help.",
        "It was my pleasure! Let me know if there's anything else.",
    ],
    "apology": [
        "I'm really sorry about that! I'll make sure to do better next time.",
        "Apologies for the confusion. I'll try again.",
        "I’m sorry for the inconvenience! How can I make it right?",
        "My bad! I didn’t mean to cause any trouble.",
    ],
    "emotions": [
        "I'm here for you. Want to talk about how you're feeling?",
        "It sounds like you're going through something. How can I support you?",
        "I'm sorry you're feeling that way. If you'd like to talk about it, I'm here.",
        "I get that. Sometimes things can be tough. How can I help?",
    ],
    "opinion": [
        "In my humble opinion, I think that’s a great idea!",
        "That sounds like a fantastic plan to me!",
        "I believe you're onto something good with that.",
        "I think you're on the right track there!",
    ],
}

def get_response(category):
    return random.choice(responses.get(category, ["I'm not sure how to respond to that."]))

def chatbot():
    print("Hello! I’m your chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "quit":
            print("Goodbye! Have a great day!")
            break
        
        if "hello" in user_input or "hi" in user_input or "hey" in user_input:
            response = get_response("greeting")
        elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
            response = get_response("farewell")
        elif "help" in user_input:
            response = get_response("help")
        elif "joke" in user_input or "funny" in user_input:
            response = get_response("joke")
        elif "how" in user_input or "doing" in user_input or "today" in user_input:
            response = get_response("small_talk")
        elif "thank" in user_input or "thanks" in user_input:
            response = get_response("gratitude")
        elif "sorry" in user_input:
            response = get_response("apology")
        elif "feel" in user_input or "emotion" in user_input or "sad" in user_input or "happy" in user_input:
            response = get_response("emotions")
        elif "opinion" in user_input or "think" in user_input:
            response = get_response("opinion")
        else:
            response = get_response("error")
        
        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
