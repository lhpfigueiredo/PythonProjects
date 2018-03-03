from MessageBusServer import MessageBusServer
from SimpleMessageFactory import SimpleMessageFactory

class MessageBusClient:

    messageBusServer = None

    publishersList = []
    messageBuffer = []

    def __init__(self, messageBusServer):
        messageBusServer.addSubscriber(self)

    def __del__(self):
        if self.messageBusServer is not None:
            self.messageBusServer.removeSubscriber(self)

    def update(self, messageContent):
        msgFactory = SimpleMessageFactory()
        msg = msgFactory.recreateMessage(messageContent)
        print(msg.getContent())
