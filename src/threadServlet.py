#importing libraries
import socket
import threading

class myThread (threading.Thread):

	def __init__(self, threadID, name, connectionSocket,addr):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.connectionSocket = connectionSocket
		self.addr = addr

	def run(self):
		serve(self,self.connectionSocket)
		self.connectionSocket.close()

def serve(thread,connection):

    #Terminate the connection
	connection.close()

