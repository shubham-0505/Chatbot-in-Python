def chatbot():
    responses = {
        "hello": "Hi! How can I help you?",
        "how are you?": "I'm doing well, thank you! How about you?",
        "what is your name?": "My name is Virtual Assistant. Nice to meet you!",
        "bye": "Have a nice day!",
        "default": "I'm sorry, I didn't understand that. Can you please rephrase?"
    }

    print("Assistant: Hi! How can I assist you today?")

    while True:
        user_input = input("User: ").lower()

        if user_input in responses:
            print("Assistant:", responses[user_input])
        else:
            print("Assistant:", responses["default"])

        if user_input == "bye":
            break

chatbot()
