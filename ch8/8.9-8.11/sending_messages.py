text_messages = ['Whatre you up2?', 'I am at the movies', 'I am at the gym']
sent_messages = []


def show_messages(messages):
    """Print all messages in the list"""
    for message in messages:
        print(message)


show_messages(text_messages)


def send_messages(messages, sent_messages_list):
    """Individually print each message, and then move it to sent_messages"""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages_list.append(current_message)


# send_messages(text_messages, sent_messages)

# print(f"\nFinal lists: {text_messages} {sent_messages}")


# 8.11 Archived Messages - call send_messages() using a copy of text_messages

send_messages(text_messages[:], sent_messages)
print(f"\nFinal lists:\n{text_messages} \n{sent_messages}")