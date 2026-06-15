print("ChatBot: Hi! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("ChatBot: Hello! How are you?")
    elif user == "how are you":
        print("ChatBot: I am fine. Thank you!")
    elif user == "bye":
        print("ChatBot: Goodbye!")
        break
    else:
        print("ChatBot: Sorry, I don't understand.")
