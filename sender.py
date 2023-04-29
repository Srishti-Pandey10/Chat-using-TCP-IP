import socket
s= socket.socket()
print('Socket Created in server')
s.bind(('localhost',9999) ) 

s.listen()
print('waiting for connections')

c, addr = s.accept()
print('Reciever connected with ', addr,end="\n")

while(True):
    msg_from_reciever = c.recv(1024).decode()
    if msg_from_reciever == 'stop' or msg_from_reciever == 'STOP':
        print("Client Disconnected\n")
        break
    print("Receiver: {}".format(msg_from_reciever))
    msg_from_sender = input("Sender:")
    if msg_from_sender == 'stop' or msg_from_sender == 'STOP':
        c.send(bytes("Server Stopped", 'utf-8'))
        break
    c.send(bytes(msg_from_sender,'utf-8'))
    
print('Connection Closed')
s.close()