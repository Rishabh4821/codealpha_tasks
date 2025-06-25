def chatbot():
    print("🤖 ChatBot: Hello! I'm your simple chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("🤖 ChatBot: Hi there! 👋")
        elif user_input == "how are you":
            print("🤖 ChatBot: I'm doing great! Thanks for asking. 😊")
        elif user_input == "bye":
            print("🤖 ChatBot: Goodbye! Have a nice day! 👋")
            break
        elif user_input == "what is your name":
            print("🤖 ChatBot: I'm a simple chatbot created in Python.")
        elif user_input == "who created you":
            print("🤖 ChatBot: I was created by a Python programmer like you!")
        elif user_input == "what can you do":
            print("🤖 ChatBot: I can chat with you, answer basic questions, and make you smile. 😄")
        elif user_input == "tell me a joke":
            print("🤖 ChatBot: Why don’t scientists trust atoms? Because they make up everything! 😂")
        elif user_input == "what's the time":
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"🤖 ChatBot: The current time is {now}")
        elif user_input == "thank you":
            print("🤖 ChatBot: You're welcome! 😊")
        elif user_input == "help":
            print("🤖 ChatBot: Here are some things you can ask me:\n"
                  "- hello\n- how are you\n- what is your name\n- who created you\n"
                  "- what can you do\n- tell me a joke\n- what's the time\n- thank you\n- bye")
        else:
            print("🤖 ChatBot: I'm not sure how to respond to that. Type 'help' to see what I can do.")

# Run the chatbot
chatbot()