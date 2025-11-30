messages=['Hello','Bye','How are you?','Good morning','You are welcome']
def show_message(messages):
    while  messages:
        print(messages.pop())
show_message(messages)