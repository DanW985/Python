class Notification(object):   

    def __init__(self, user, message):
        self.user = user
        self.message = message
        self.items = [] #no problem?

    def send_message(self):
        print('Message sent to {}: {}'.format(self.user, self.message))

    def change_user(self, user):
        self.user = user
    
    def change_message(self, message):
        self.message = message

n = Notification('joe', 'The message.')
m = Notification('jane', 'Another message.')

n.send_message()
m.send_message()
m.change_user('bob')
m.send_message()
m.change_message('This message.')
m.send_message()

print(m.items)
m.items.append('some item')
print('n items? ' + str(n.items))
