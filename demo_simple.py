from process_message_system import *
import sys

class Consumer(MessageProc):

    def main(self):
        super().main()
        
        n=0

        while True:
            self.receive(
                Message(
                    'data',
                    action=lambda x: print(x)),
                Message(
                    'stop',
                    action=lambda: sys.exit()))
            n=n+1
            if n==1000:
                print("it was stuck")
                break;

if __name__=='__main__': # really do need this
    me = MessageProc()
    me.main()
    consumer = Consumer().start()
    for num in range(1000):
        me.give(consumer, 'data', num + 1)
    me.give(consumer, 'stop')