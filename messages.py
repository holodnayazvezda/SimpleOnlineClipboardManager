def get_messages(filename):
    f = open(filename, mode='r+', encoding='utf-8')
    data = f.read()
    messages = list(filter(lambda el: el, map(lambda el: el.strip(), data.split('!!!'))))
    f.close()
    return messages


def add_message(filename, message_text):
    messages = get_messages(filename)
    f = open(filename, mode='w+', encoding='utf-8')
    # добавить message_text, так чтобы старые данные не удалялись
    for message in messages:
        print(message)
        f.write(message +'\n!!!')
    f.write(message_text + '\n!!!')
    f.close()