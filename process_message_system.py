import sys
import os
import pickle
import time


class MessageProc():

	#set up communication mechanism (named pipes)
	def main (self):
		print("main method in parent")
		
		#create named pipe
		os.mkfifo('/tmp/pipe'+str(os.getpid()))

	




	#start up a new process and return process id to parent process
	def start(self):		

		#fork
		pid = os.fork()
		
		#If child fork
		if pid == 0:
			#go into the main()
			self.main()
			
		#if parent fork
		else:
			#return pid of the child fork
			return pid



	#send the input parameter message items it receives to the recieve()
	#pid - pid of child fork 
	#messageID - id type of message sent (what is checked in recieve)
	#values - not nessary to pass in
	def give(self, pid, messageID, *values):

		pipe = '/tmp/pipe'+str(pid)
		
		#check communitcation process is up else sleep for a bit
		if not os.path.exists(pipe):
			time.sleep(0.5)
		
		fifo = open(pipe,'wb')
		
		#parent fork gives the message
		
		tup = []
		tup.append(pid)
		tup.append(messageID)
		tup.append(values)
		pickle.dump(tup,fifo)
		#check communitcation process is up else sleep for a bit
		
		
		#parent fork gives the message
		
		#print('in give()')
		#print('messageID is '+str(messageID))
		
		pass



#check out os atExit and clean up named pipes

	#check message does not exist in queue and remove executed messages
	def receive(self, *messages):

		pipe = '/tmp/pipe' + str(os.getpid())

		# check communitcation process is up else sleep for a bit
		if not os.path.exists(pipe):
			time.sleep(0.5)

		fifo = open(pipe, 'r')


		#for line in
		
		
		#child fork recieves the message
		
		for mess in messages:
			
			#if message ID is ANY then execute first item in give queue
			if mess.messageID == 'ANY':
				pass
			
			else:
				pass
			
			
			#put time out here
			
		pass

	#what to do when system ends
	def removeGarbage(self):
		pass
		#remove all pipes
	
	#import atexit
	#atexit.register(removeGarbage())

class Message():
	
	def __init__(self,messageID, action):
		
		self.messageID = messageID
		self.action=action
		
		#pass
		
class TimeOut():
	pass