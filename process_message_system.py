import sys
import os
import pickle
import time
import threading
import atexit
import queue

ANY = 'any'


class MessageProc():
    communcation_queue = queue.Queue()
    passed_data_list = []

    # set up communication mechanism (named pipes)
    def main(self):

        # create named pipevalue =
        os.mkfifo('/tmp/pipe' + str(os.getpid()))

        # Get threading condition - robert lecture
        self.arriveCondition = threading.Condition()

        # set up thread
        transfer_thread = threading.Thread(target=self.extract_from_pipe, daemon=True)
        transfer_thread.start()

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

        if values:
            tup.append(*values)

        pickle.dump(tup, fifo)




    # check message does not exist in queue and remove executed messages
    def receive(self, *messages):

        # From rob's code in lecture recording 9
        while True:

            # Check if queue is not empty, else wait for thread condition
            if not self.communcation_queue.empty():

                # get data from queue
                data = self.communcation_queue.get()

                self.communcation_queue.task_done()

                for mess in messages:

                    if mess.messageID == ANY or data[1] == mess.messageID:

                        # if there is no value given
                        if len(data) == 2:
                            value = mess.action()

                        else:
                            value = mess.action(data[2])

                        return value

                    #not what we want so put unused data into list
                    else:
                        self.passed_data_list.append(data)
                        # self.passed_data_list.insert(data)


            elif self.communcation_queue.empty() and self.passed_data_list:

                while True:
                    self.passed_data_list.reverse()
                    item = self.passed_data_list.pop()
                    self.communcation_queue.put(item)
                    if not self.passed_data_list:
                        break


            else:
                # From Tutorial 3 code
                # Automatic acquire/release of the underlying lock
                with self.arriveCondition:

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
                        self.communcation_queue.put(message)
                        self.arriveCondition.notify()

                except EOFError:
                    time.sleep(0.01)


# what to do when system ends
def removeGarbagePipes ():
    tmpPath = '/tmp'
    files = os.listdir('/tmp')
    for file in files:
        if file.startswith('pipe'):
            os.remove(tmpPath + '/' + file)

#at end of process do this
atexit.register(removeGarbagePipes)


class Message():
    def __init__(self, messageID, action):
        self.messageID = messageID
        self.action = action

        # pass


class TimeOut():
    pass
