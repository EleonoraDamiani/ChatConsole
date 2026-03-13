import socket

HOST = '127.0.0.1'  # server IP
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input("Client: ")
    client.sendall(msg.encode())
    data = client.recv(1024).decode()
    print("Server:", data)
