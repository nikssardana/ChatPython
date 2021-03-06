#!/usr/bin/python

import socket
import sys
import os

def listen1():
	while True:	
		try:
			message1 = connection1.recv(180)
                        
                        if message1 ==  '\q':
                            connection2.send(message1)
                            connection1.shutdown(socket.SHUT_RD | socket.SHUT_WR)		
                            connection2.shutdown(socket.SHUT_RD | socket.SHUT_WR)
                            connection1.close()
                            connection2.close()
                            server.close()
                            print "Connections closed"
                            break

                           
			if message1:
				connection2.send(message1)
				print "message",message1,'sent from client1 to client2'
		
		except:
                    try:
                            connection1.shutdown(socket.SHUT_RD | socket.SHUT_WR)		
                            connection2.shutdown(socket.SHUT_RD | socket.SHUT_WR)
                            connection1.close()
                            connection2.close()
                            server.close()
                            print "An error occured. Connections closed"
                            break
                    except:
                        pass

	
def listen2():
	while True:	
		try:
			message2 = connection2.recv(180)
                        if message2 ==  '\q':
                            connection1.send(message2)
                            connection1.shutdown(socket.SHUT_RD | socket.SHUT_WR)		
                            connection2.shutdown(socket.SHUT_RD | socket.SHUT_WR)
                            connection1.close()
                            connection2.close()
                            server.close()
                            print "Connections closed"
                            break

			if message2 != ' ':
				connection1.send(message2)
				print "message",message2,'sent from client2 to client1'
		
		except:
                    try:
                            connection1.shutdown(socket.SHUT_RD | socket.SHUT_WR)		
                            connection2.shutdown(socket.SHUT_RD | socket.SHUT_WR)
                            connection1.close()
                            connection2.close()
                            server.close()
                            print "An error occured. Connections closed"
                            break
                    except:
                        pass



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server_address = ('192.168.1.6',8081)
server.bind(server_address)
print "Server started on port 8081"

server.listen(2)	#listens for connection request from clients
connection1,client_address1 = server.accept()	#accepts a request from client
print 'client1:',connection1.getpeername()

server.listen(2)	#listens for connection request from clients
connection2,client_address2 = server.accept()	#accepts a request from client
print 'client2:',connection2.getpeername()

newpid = os.fork()

if newpid == 0:	#child process
	listen1()
	parentId = os.getppid()
	os.kill(parentId,signal.SIGKILL)

	
else:
	listen2()
