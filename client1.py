#!/usr/bin/python

import socket
import os
import sys

client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client1.connect(('192.168.1.6',8081))	#ip address of machine where server is running

def inp():
	while True:
		message = raw_input('Me: ')
		if message:
			client1.send(message)					

def outp():
	while True:
		data = client1.recv(180)
		if data:
			print '\nReceived: ',data

newpid = os.fork()

if newpid == 0:
	inp()
else:
	outp()
