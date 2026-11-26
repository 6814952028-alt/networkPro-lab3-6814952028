import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(5)

print("Socket server is running and waiting for connections...", flush=True)

while True:
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}", flush=True)

    data = conn.recv(1024).decode()
    print(f"Received message: {data}", flush=True)

    response = f"Echo: {data}"
    conn.sendall(response.encode())

    conn.close()