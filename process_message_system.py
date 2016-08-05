import sys
import os

class MessageProc():

	#set up communication mechanism (named pipes)
	def main (self):
		print("main method")

	




	#start up a new process and return process id to parent process
	def start(self):
		

		#fork
		pid = os.fork()

		if pid == 0:
			print("child")

			

			#kill child for now
			sys.exit(0)
		else:
			print("parent")

		#child calls main()



		#return process id of child to parent process
		#return




	#send the input parameter message items it receives to the recieve()
	def give(self, pid, messageID, *values):
		pass





	#check message does not exist in queue and remove exectued messages
	def recieve(self):
		pass


class Message():

	#class constructor
	def _init_(self,messageID, messageAction):
		pass


class TimeOut():
	pass



