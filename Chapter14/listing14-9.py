from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver


class SimpleLogger(LineReceiver):

    def connectionMade(self):
#@#         print 'Got connection from', self.transport.client
        print('接続受付：', self.transport.client)

    def connectionLost(self, reason):
#@#         print self.transport.client, 'disconnected'
        print(self.transport.client, '接続解除')
        

    def lineReceived(self, line):
        print(line)

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()
