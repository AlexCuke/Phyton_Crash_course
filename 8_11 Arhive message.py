messages1=['Hello','Bye','How are you?','Good morning','You are welcome']
'''def show_message(messages):
    while  messages:
        print(messages.pop())
show_message(messages1)'''
print()
def send_message(messages):
    sent_messages=[]
    while messages:
        message=messages.pop()
        print(message)
        sent_messages.append(message) 
    print('Все сообщения отправлены')
    print(messages1)
    print(sent_messages)
send_message(messages1[:])