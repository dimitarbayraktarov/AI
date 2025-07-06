import random

responses = ["meow", "purr", "hiss", "scratch", ":3", "nya", "nya nya", "nya nya nya",
             "nya nya nya nya", "nya nya nya nya nya", "*tummy rub*",
             "*pisses on your leg*", "head butt", "*tail wag*", "poop", "meow meow",
             "meow meow meow", "meow meow meow meow", "meow meow meow meow meow",
             "*poops on your keyboard*", "*begs for food*", "*chases laser pointer*", 
             "*sleeps on your keyboard*", "*scratches the couch*", "*plays with yarn*",
             "*catches a mouse*", "*watches birds*", "*paws at the window*",
             "*rolls over*", "*grooms itself*", "*pounces on a toy*", "*meows softly*",
             "*purrs loudly*", "*stretches*", "*chases tail*", "*sits in a box*",
             "*hides in a bag*", "*curls up in your lap*",
             "gives you a slow blink", "*rubs against your leg*"]

def get_random_response():
    return random.choice(responses)

if __name__ == "__main__":
    print("meow! i'm catbot! type 'meow' to start chatting with me! type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye"]:
            print("CatBot: bye! :3")
            break
        response = get_random_response()
        print(f"CatBot: {response}")