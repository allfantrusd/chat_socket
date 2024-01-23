import socket
import keyboard as key

def client(host: str, port: int):
    client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = (host, port)
    client_soc.connect(server_addr)
    print(f"[*] Successfully connected to the server ...")

    try:
        while True:
            key.wait("g")
            if not key.is_pressed("g"):
                # Receive the response from the server
                recv_data = client_soc.recv(1024)
                print(f"[*] Received data: {recv_data.decode('utf-8')}")
            else:
                data = input("Enter the data to send (or type 'exit' to quit): ") or "N/A"
                if data.lower() == "exit":
                    break
                # Send data to the server
                client_soc.sendall(data.encode('utf-8'))
            
            
    finally:
        client_soc.close()

if __name__ == "__main__":
    host ="server addr"
    port = 8080
    client(host, port)
