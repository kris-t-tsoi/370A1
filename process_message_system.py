import sys
import os
import pickle
import time
import threading
import atexit
import queue

#SOFTENG 370
#Yee Wing Kristy Tsoi
#ytso868
#6521229

#state global variables
ANY = 'any'


#------------------------------------------------------------------------------------
class MessageProc():

    #queue and list to store give() data
    data_list = []

    # set up communication mechanism
    def main(self, *process):

        # create named pipe
        pipe = '/tmp/pipe' + str(os.getpid())
        if not os.path.exists(pipe):
            os.mkfifo(pipe)


        # Get threading condition - robert lecture
        self.arriveCondition = threading.Condition()


        # set up thread
        transfer_thread = threading.Thread(target=self.extract_from_pipe, daemon=True)
        transfer_thread.start()

        # at end of process do this
        atexit.register(removeGarbagePipes)



    # start up a new process and return process id to parent process
    def start(self, *processes):

        # fork
        pid = os.fork()

        # If child fork
        if pid == 0:
            # go into the main()
            self.main(*processes)

            time.sleep(0.1)
            sys.exit()

        # if parent fork
        else:
            # return pid of the child fork
            return pid



    # send the input parameter message items it receives to the recieve()
    # pid - pid of child fork
    # messageID - id type of message sent (what is checked in recieve)
    # values - not nessary to pass in
    def give(self, pid, messageID, *values):

        # check communication process is up else sleep for a bit
        pipe = '/tmp/pipe' + str(pid)
        if not os.path.exists(pipe):
            time.sleep(0.05)

        fifo = open(pipe, 'wb')

        #put data into pipe
        pickle.dump([messageID, values], fifo)


    # check message does not exist in queue and remove executed messages
    def receive(self, *messages):

        #Each timeout is unique to each recieve
        timeoutValue = None
        timeoutAction = None

        #Check if there a Timeout object
        for mess in messages:
            # Check if message is a Timeout
            if type(mess) == TimeOut:
                timeoutValue = mess.waitTime
                timeoutAction = mess.action


        # From rob's code in lecture recording 9
        while True:

            for item in self.data_list:
                # compare give() data to messages recieved by recieve()
                for mess in messages:
                    # Check if it is the correct message
                    if (mess.messageID == ANY or item[0] == mess.messageID) and mess.guard():
                        self.data_list.remove(item)
                        return mess.action(*item[1])


            # From Tutorial 3 code
            # Automatic acquire/release of the underlying lock
            with self.arriveCondition:
                
                #if there was a timeout message
                if not timeoutValue == None:
                    startTime = time.time()
                    self.arriveCondition.wait(timeoutValue)
                    finishTime = time.time()

                    timeoutValue = timeoutValue - (finishTime-startTime)

                    if not timeoutValue <= 0:
                        return timeoutAction()

                else:
                    # notify the waiting thread that the resource is now ready
                    self.arriveCondition.wait()



    # taken from Robert's lecture recording 9 video
    def extract_from_pipe(self):

        pipe = '/tmp/pipe' + str(os.getpid())

        with open(pipe, 'rb') as readPipe:
            while True:
                try:
                    message = pickle.load(readPipe)
                    with self.arriveCondition:
                        self.data_list.append(message)
                        self.arriveCondition.notify()

                except EOFError:
                    time.sleep(0.01)



# ------------------------------------------------------------------------------------
# called when system ends to delete pipes
def removeGarbagePipes ():

    time.sleep(.15)

    tmpPath = '/tmp'
    files = os.listdir('/tmp')
    for file in files:
        if file.startswith('pipe'):
            os.remove(tmpPath + '/' + file)


#------------------------------------------------------------------------------------
class Message():
    def __init__(self, messageID, guard = lambda: True, action= lambda: None):
        self.messageID = messageID
        self.action = action
        self.guard = guard

        # pass

#------------------------------------------------------------------------------------
class TimeOut():

    def __init__(self, waitTime, action=lambda: None):
        self.waitTime = waitTime
        self.action = action