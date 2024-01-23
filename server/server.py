import socket
import threading

def handle_client(client_socket, address, clients):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            message = f"{address[0]}:{address[1]} says: {data.decode('utf-8')}"
            print(message)

            # Broadcast the message to all clients except the sender
            for c in clients:
                if c != client_socket: # except the sender condition
                    try:
                        c.sendall(message.encode('utf-8'))
                    except:
                        # Remove broken connections
                        clients.remove(c)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Remove the client from the list
        clients.remove(client_socket)
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8080)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print(f"Server listening on {server_address}")

    clients = []

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            clients.append(client_socket)

            # Create a thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, clients))
            client_thread.start()

    except KeyboardInterrupt:
        print("Server shutting down.")
        server_socket.close()

if __name__ == "__main__":
    main()
