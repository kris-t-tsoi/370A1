import sys
import os

class MessageProc():

	#set up communication mechanism (named pipes)
	def main (self):
		print("main method in parent")

	




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
	def give(self, pid, messageID, *values):
		
		#parent fork gives the message
		
		pass





	#check message does not exist in queue and remove exectued messages
	def recieve(self):
		
		#child fork recieves the message
		
		pass
		#when all messages have been exceuted then close the child and parent fork named pipes


class Message():

	#class constructor
	def _init_(self,messageID, messageAction):
		pass


class TimeOut():
	pass



