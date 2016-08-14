import sys
import os

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
			#return pid of the parent fork
			return os.getpid()



	#send the input parameter message items it receives to the recieve()
	#pid - pid of fork that sent the message
	#messageID - id type of message sent (what is checked in recieve)
	#values - not nessary to pass in
	def give(self, pid, messageID, *values):
		
		#parent fork gives the message
		
		#print('in give()')
		#print('messageID is '+str(messageID))
		
		pass





	#check message does not exist in queue and remove executed messages
	def receive(self, *messages):
		
		#print('in recieve')
		
		#child fork recieves the message
		
		#for mess in messages:
			#print('message action '+str(mess.messAction))
				
				#if message ID is ANY then execute first item in give queue
				#if mess.messageID == 'ANY'
		
		pass
		


class Message():
	
	def __init__(self,messageID, action):
		
		pass
		
		
		#self.messageID = messageID
		#self.action=action
		
		#print('messAction '+str(messAction))
		#pass
		
class TimeOut():
	pass