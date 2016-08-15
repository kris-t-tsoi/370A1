import sys
import os
import pickle
import time
import threading


class MessageProc():

    def __init__(self):
        # Get threading condition
        #self.messageCondition = threading.Condition()
        pass


    # set up communication mechanism (named pipes)
    def main(self):

        # create named pipe
        os.mkfifo('/tmp/pipe' + str(os.getpid()))

        # set up thread
        #read_thread = threading.Thread(target=self.receive, daemon=True)
        #read_thread.start()



    # start up a new process and return process id to parent process
    def start(self):

        # fork
        pid = os.fork()

        # If child fork
        if pid == 0:
            # go into the main()
            self.main()

        # if parent fork
        else:
            # return pid of the child fork
            return pid


    # send the input parameter message items it receives to the recieve()
    # pid - pid of child fork
    # messageID - id type of message sent (what is checked in recieve)
    # values - not nessary to pass in
    def give(self, pid, messageID, *values):

        pipe = '/tmp/pipe' + str(pid)

        # check communitcation process is up else sleep for a bit
        if not os.path.exists(pipe):
            time.sleep(0.01)

        fifo = open(pipe, 'wb')

        # parent fork gives the message

        tup = []
        tup.append(pid)
        tup.append(messageID)
        tup.append(values)
        pickle.dump(tup, fifo)

        print(tup)


        # From Tutorial 3 code
        # Automatic acquire/release of the underlying lock
       # with self.messageCondition:
            # notify the waiting thread that the resource is now ready
        #    self.messageCondition.notify()


        # parent fork gives the message

        # print('in give()')
        # print('messageID is '+str(messageID))

        #pass

    # check out os atExit and clean up named pipes

    # check message does not exist in queue and remove executed messages
    def receive(self, *messages):

        pipe = '/tmp/pipe' + str(os.getpid())

        print('in receive')

        # check communitcation process is up else sleep for a bit
        if not os.path.exists(pipe):
            time.sleep(0.01)


        fifo = open(pipe, 'rb')

        #From rob's code in lecture recording 9
        while True:
            #wait for data to be in pipe
            message = pickle.load(fifo)

            print('receive'+str(message))
            print('pid ' + str(message[0]))
            print('data ' + str(message[1]))
            print('value ' + str(message[2]))


            for mess in messages:
                if mess.messageID == 'ANY':
                    mess.action()
                elif mess.messageID == message[1]:
                    print('match')
                    print(str(mess.action))
                    print(message[2])
                else:
                    pass




            # From Tutorial 3 code
            # Automatic acquire/release of the underlying lock
           # with self.messageCondition:
                # notify the waiting thread that the resource is now ready
            #    self.messageCondition.wait()







        # child fork recieves the message

        #for mess in messages:

            # if message ID is ANY then execute first item in give queue
         #   if mess.messageID == 'ANY':
          #      pass

           # else:
            #    pass




            # put time out here

        pass

    # what to do when system ends
    def removeGarbage(self):
        pass

    # remove all pipes

    # import atexit
    # atexit.register(removeGarbage())


class Message():
    def __init__(self, messageID, action):
        self.messageID = messageID
        self.action = action

    # pass


class TimeOut():
    pass
