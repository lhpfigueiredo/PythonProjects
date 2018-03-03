from MessageBusServer import MessageBusServer
from MessageBusClient import MessageBusClient
from SimpleMessageFactory import SimpleMessageFactory

def main():
    MsgBusServer = MessageBusServer()
    MsgBusClient1 = MessageBusClient(MsgBusServer)
    MsgBusClient2 = MessageBusClient(MsgBusServer)

    msgFactory = SimpleMessageFactory()

    msg = msgFactory.createNewMessage()
    msg.setContent('Ola Mundao!')

    MsgBusServer.post(msg.getContent())





if __name__ == "__main__":
    main()