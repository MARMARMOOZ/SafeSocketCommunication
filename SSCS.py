#SafeSocketComm. Server
import socket #for recv. and send massage on network need it
import Encrypt
import Decrypt
import base64
#insert things on there.
SERVER_IP = ""
PORT = 86
password = 808
#-----------------------
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((SERVER_IP, PORT))
ss.listen(1)
	
client, address = ss.accept()
client.send(b"0110")
recived_packet = client.recv(1024)
if recived_packet == b"1001":
	print("Connection is stable!")
	client.send(b"0110")
else:
	ss.close()
	print("invalid client!")
#-------
def send():
	msg = input()
	e1msg = Encrypt.Encrypt(msg, password)
	e2msg = base64.b64encode(e1msg.encode())
	client.send(e2msg)
def recv():
	msg = client.recv(1024)
	d1msg = base64.b64decode(msg).decode()
	d2msg = Decrypt.Decrypt(d1msg, password)
	print(d2msg)

while True:
	send()
	recv()
#-------
ss.close()
