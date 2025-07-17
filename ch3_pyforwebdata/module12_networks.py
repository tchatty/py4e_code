#Network architecture
#Transport control protocol provides a pipeline between two applications. Ignore the internet and link layers for now.
#A port is an application specific end point. Connect with port 80 - http
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM refers to TCP and AF_INET refers to IPv4
mysock.connect(('data.pr4e.org',80)) #this makes the socket connection
#HTTP - dominant application layer protocol on the internet. Rules to allow browsers to retrieve information from the internet.
#url - uniform resource locator
#The request response cycle: Get command sends the link to the server which returns the html file for the response.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
response = b"" #byte string
while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    response += data
parts = response.decode().split('\r\n\r\n',1)
if len(parts) ==2:
    header = parts[0]
    # with open('romeo.txt','w') as f: #with is the best practice for working with files because it makes sure files are closed after use.
    #     f.write(body)
    print(header)
else:
    print('No header found in response')
mysock.close()