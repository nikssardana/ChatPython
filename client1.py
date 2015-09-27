#!/usr/bin/python

import socket
import os
import sys
import signal

client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client1.connect(('192.168.1.6',8081))	#ip address of machine where server is running

def inp():
	while True:
            try:
		message = raw_input('Me: ')
		if message:
			client1.send(message)					
                        if message == '\q':
                            print "<--Exiting... Goodbye! -->"
                            break
                         	
            except:
                break

def outp():
	while True:
		data = client1.recv(180)
		if data:
                    if data == '\q':
                        print "<--Exiting... Goodbye! -->"
                        break
                    print '\nReceived: ',data
                        

newpid = os.fork()

if newpid == 0:	#child process
	outp()
	parentId = os.getppid()
	os.kill(parentId,signal.SIGKILL)	#kill parent, then exit
	
else:
	inp()
	parentId = os.getpid()
	os.kill(parentId,signal.SIGKILL)
