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


def put():
    pass

def get():
    pass

def clear():
    pass

def quit():
    pass

"""
    <name>
        identify_command

    <purpose>
        Given a line from the client, the server attempts to identify
        which command was requested. The accompanying parameters are also
        bundled so that the worker thread can feed it to the necessary 
        routine. 

        Sanitization of special commands is not done here

    <parameters>
        input_string: the actual line coming from the client

    <returns>
        None 
            in case the requested function is malformed (e.g. command doesn't
            exist). Commands are case-sensitive.

            or if a string with a wrong length (0 or above 200) is given

            or if a string with unicode is given



        A tuple with function to run and a list of arguments to feed
        such function.

"""
def identify_command(input_string):
        
    # we will use a list of available commands to search through, this
    # is case sensitive
    available_commands = {'PUT': put,
            'GET': get,
            'CLEAR': clear,
            'QUIT':quit}

    
    # Input sanitization
    # FIXME: maybe should raise an exception
    if input_string is None:
        return None
 
    if len(input_string) > 200:
        return None

    try:
        input_string.decode('ascii')

    except UnicodeDecodeError:
        return None
 
    # split the input string 
    arguments = input_string.split(' ')
    
    command = arguments[0]

    if command not in available_commands:
        return None

    # remove the command from the arguments
    arguments.pop(0)

    return (available_commands[command],  arguments)
