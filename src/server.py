#import socket module
import socket
import threadServlet
import threading

# the server class, runs on a separate thread to work as a daemon
class afp_server(threading.Thread):
   
    # initialize, the max_connection parameter provides a way to kill the daemon
    # by connecting/disconnecting multiple times, send a negative to loop endlessly 
    # (or for quite a while)
    def __init__(self, max_connections):

        threading.Thread.__init__(self)

        #prepare the server socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.port = 9000

        # set to negative for endless loop
        self.max_connections = max_connections

    
    def run(self):

        #These params will let us close and open the server without waiting for a flush.
        self.serverSocket.bind(('',self.port))  #binding to a port
        self.serverSocket.listen(1)             #listening on port

        i = 0

        print('ready to serve...')

        #start of main loop, remember, negative is infinite whoa.jpg
        while i < self.max_connections:

            #establish the connection
            connectionSocket, addr = self.serverSocket.accept() #receive a connection

            t = threadServlet.myThread(i, "socket", connectionSocket,addr)

            i+=1

            t.start()

        # we are done serving, so we must shut up
        self.serverSocket.close()

if __name__=="__main__":
    afp_server()
