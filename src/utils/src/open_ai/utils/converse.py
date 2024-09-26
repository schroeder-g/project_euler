from classes import Chat as OAIC, Message as OAIM

Chat = OAIC.Open_AI_Chat
Message = OAIM.OAIMessage


def converse(chat):
    introduction_string = """
        Beginning interactive session. You have a couple of options:
         - Type a message and press enter to get a response.
         - Type 'quit' to exit the interactive session.
         - Type 'help' to get help.
         - Type 'functions' to get a list of available functions.
         - Type 'set' and a parameter name to set a parameter.
         - Type 'get' and a parameter name to get a parameter.
         - Type 'History' to get a list of previous messages.
        """

    print(introduction_string)
    while True:
        # Get user input
        user_input = input("User: ")
        if user_input == "quit":
            break
        elif user_input == "help":
            print(introduction_string)
            continue
        elif user_input == "functions":
            print(
                "Available functions (This doesn't work): ",
                ", ".join([func for func in dir(Chat) if "__" not in func]),
            )
            continue
        elif "set " in user_input[:4]:
            # Set parameter
            param = user_input[4:]
            if param in params:
                print(f"Setting {param} to {getattr(chat, param)}")
                chat.__setattr__(param, input(f"Enter new value for {param}: "))
                continue
            else:
                print(f"Error: {param} is not a valid parameter.")
                continue
            continue
        elif "get " in user_input[:4]:
            # Get parameter
            param = user_input[4:]
            if param in params:
                print(f"{param} is set to {getattr(chat, param)}")
                continue
            else:
                print(f"Error: {param} is not a valid parameter.")
                continue
            continue
        elif user_input == "History":
            print("___History___\n", chat.history)
            continue

        # Create user message
        user_message = Message.create("user", user_input)

        # Create messages list
        messages = [chat.system, user_message]

        # Get number of tokens
        num_tokens = num_tokens_from_messages(messages)

        # Create completion
        completion = chat.completion(messages=messages, num_tokens=num_tokens)

        # Get response
        response = Message.response(completion)
