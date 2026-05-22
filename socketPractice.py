import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://https://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode() # http rules require a blank line after the header, so we add \r\n\r\n to the end of the command. 
# We also need to encode the string into bytes before sending it to the server. encode is a set of UTF-8 bites that can be decoded back into a string.
mysock.send(cmd) # file handler

while True:  
    data = mysock.recv(512) # upto 512 characters at a time
    if (len(data) <1 ): # if there is no data, we are done and can exit the loop
        break
    print(data.decode()) # decode UTF-8 the bytes back into a string and print it out.
mysock.close() # closing connection to the server.

