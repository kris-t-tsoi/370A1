import sys
import os
import pickle

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
			print("messageproc child fork pid", os.getpid())
			#go into the main()
			self.main()
			
		#if parent fork
		else:
			print("parent")
			print("messageproc parent fork pid", os.getpid())
			#return pid of the child fork
			return pid



	#send the input parameter message items it receives to the recieve()
	#pid - pid of child fork 
	#messageID - id type of message sent (what is checked in recieve)
	#values - not nessary to pass in
	def give(self, pid, messageID, *values):
		
		#check communitcation process is up else sleep for a bit
		
		
		#parent fork gives the message
		
		
		
		#print('in give()')
		#print('messageID is '+str(messageID))
		
		pass



#check out os atExit and clean up named pipes

	#check message does not exist in queue and remove executed messages
	def receive(self, *messages):
		
		
		
		#child fork recieves the message
		
		for mess in messages:
			
			#if message ID is ANY then execute first item in give queue
			if mess.messageID == 'ANY':
				pass
			
			else:
				pass
			
			
			#put time out here
			
		pass
		
		


class Message():
	
	def __init__(self,messageID, action):
		
		self.messageID = messageID
		self.action=action
		
		#pass
		
class TimeOut():
	pass