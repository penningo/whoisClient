#!/usr/bin/env python

import socket
import sys

class whois(object):
        
    #Server settings
    WHOISSERVER = "whois.ripe.net"

    #Ripe Response
    ripeResponse = {}

        #initialisation
    def __init__(self, query, printOut=True):
        self.ripeResponse["response"] = self.ripeQuery(query)
        if printOut:
            for line in self.ripeResponse["response"]:
                print line
        else:
            self.processOutput()

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

    def processOutput(self):
        processed = {}
        for line in self.ripeResponse["response"]:
            if "%" not in line:
                if line != "":
                    line = line.split(" ")
                    data = ""
                    for dataLine in line[1:]:
                        if dataLine != "":
                            data += dataLine

                    processed[line[0].replace(":", "")] = data

        self.ripeResponse["responseDict"] = processed
        return self.ripeResponse["responseDict"]

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