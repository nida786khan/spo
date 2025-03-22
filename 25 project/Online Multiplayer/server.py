import socket
import threading

HOST = "127.0.0.1"  # Localhost
PORT = 5555         # Port number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)  # Multiple players allowed

print("Server is waiting for connections...")

clients = []  # Connected players list

def handle_client(conn, addr):
    clients.append(conn)
    print(f"Player connected from {addr}")
    
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Received: {data}")
            
            # Send message to all players
            for client in clients:
                if client != conn:
                    client.send(data.encode())
        except:
            break
    
    conn.close()
    clients.remove(conn)
    print(f"Player {addr} disconnected.")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
