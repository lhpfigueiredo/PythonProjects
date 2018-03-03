from SimpleMessageFactory import SimpleMessageFactory

class MessageBusServer:

    subscribersList = []
    publishersList = []
    messageBuffer = []

    def __init__(self):
        pass

    def addSubscriber(self, subscriber):
        if self.subscribersList.count(subscriber) == 0:
            self.subscribersList.append(subscriber)

        return 0

    def removeSubscriber(self, subscriber):
        if self.subscribersList.count(subscriber) > 0:
            self.subscribersList.remove(subscriber)

        return 0

    def notifySubscribers(self):
        msg = self.messageBuffer.pop()
        for item in self.subscribersList:
            item.update(msg.getContent())

    def post(self, messageContent):
        msgFactory = SimpleMessageFactory()
        msgItem = msgFactory.recreateMessage(messageContent)
        self.messageBuffer.append(msgItem)
        self.notifySubscribers()
