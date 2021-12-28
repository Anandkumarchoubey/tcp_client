import socket

target_host = "localhost"
target_port = 9999

#create a socket object

clint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the clint

clint.connect((target_host,target_port))

#send some data
clint.send(b"GET / HTTP/1.1\r\nHost : hacker.com\r\n\r\n")

#receive some data
response = clint.recv(4096)

print(response.decode())
