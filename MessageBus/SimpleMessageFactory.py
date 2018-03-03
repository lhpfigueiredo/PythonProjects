from Message import SimpleMessage

class SimpleMessageFactory:

    def __init__(self):
        pass

    def createNewMessage(self):
        return SimpleMessage()

    def recreateMessage(self, msgContent):
        msg = SimpleMessage()
        msg.setContent(msgContent)
        return msg