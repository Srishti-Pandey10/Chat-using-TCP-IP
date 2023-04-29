import socket

s=socket.socket()
print('Socket created in Client')

s.connect(('localhost',9999))

while True:
    msg_from_reciever=input("Receiver:")
    s.send(bytes(msg_from_reciever, 'utf-8'))
    if msg_from_reciever == 'stop' or msg_from_reciever == 'STOP':
        break
    msg_from_sender=s.recv(1024).decode()
    if msg_from_sender == 'Server Stopped' or msg_from_sender == 'Server Stopped':
        print("Server closed")
        break
    print("Sender: {} ".format(msg_from_sender))
print('Connection Closed')
s.close()
