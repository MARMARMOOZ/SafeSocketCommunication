#SafeSocketComm. Client
import socket
import Encrypt
import Decrypt
import base64
#insert the things on there.
SERVER_IP = "127.0.0.1" #bro you dont need change this only give client your ip.
PORT = 86
password = 808
#---------------------------
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect((SERVER_IP, PORT))
if ss.recv(1024) == b"0110":
	ss.send(b"1001")
	if ss.recv(1024) == b"0110":
		print("Connection is stable!")
else:
	ss.close()
	print("invalid Server!")
#------
def send():
	msg = input()
	e1msg = Encrypt.Encrypt(msg, password)
	e2msg = base64.b64encode(e1msg.encode())
	ss.send(e2msg)
def recv():
	msg = ss.recv(1024)
	d1msg = base64.b64decode(msg).decode()
	d2msg = Decrypt.Decrypt(d1msg, password)
	print(d2msg)

while True:
	recv()
	send()
#------
ss.close()
