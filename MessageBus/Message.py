class IMessage:

    content = ''

    def getContent(self):
        return self.content

    def setContent(self, msgContent):
        self.content = msgContent

class SimpleMessage(IMessage):

    def __init__(self):
        pass

