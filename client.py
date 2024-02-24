import socket

HOST = '192.168.10.14'  # Replace with the IP of the server
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server. Start typing messages:")
    while True:
        message = input("> ")
        if message.lower() == 'exit':
            break
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Server says: {data.decode()}")
