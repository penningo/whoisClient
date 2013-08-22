#!/usr/bin/env python

import socket
import os
import sys

class whois:
	
	#Server settings
	WHOISSERVER = "whois.ripe.net"
	
	#Ripe Response
	ripeResponse = {}

	#initialisation
	def __init__(self, query):
		self.ripeResponse["response"] = self.ripeQuery(query)
		for line in self.ripeResponse["response"]:
			print line

	#Queries ripe db
	def ripeQuery(self, query):
		tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcpSocket.connect((self.WHOISSERVER, 43))
		tcpSocket.sendall(query + "\r\n")
		response = ""
		while True:
			data = tcpSocket.recv(1024)
			response += data
			if not data:
				break
		tcpSocket.close()
		charBuffer = ""
		returnResponse = []
		for char in response:
			charBuffer += char
			if char == "\n":
				returnResponse.append(charBuffer.rstrip("\n"))
				charBuffer = ""
		return returnResponse

if __name__ == "__main__":
	if len(sys.argv) > 1:
		string = ""
		i = 1
		while i < len(sys.argv):
			string += sys.argv[i] + " "
			i += 1
		whois(string)
	else:
		whois(raw_input("Query (Query Host = whois.ripe.net): "))