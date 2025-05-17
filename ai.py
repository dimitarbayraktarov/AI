import random

def simple_chatbot(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm just a bot, but I'm doing fine!", "I'm good! How about you?"],
        "what is your name": ["I'm a simple chatbot!", "You can call me ChatBot."],
        "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"]
    }
    
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm not sure how to respond to that."

if __name__ == "__main__":
    print("Simple ChatBot: Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print(f"ChatBot: {response}")