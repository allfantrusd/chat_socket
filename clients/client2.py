import socket
import time
import sys

def client(host: str, port: int):
    client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = (host, port)
    client_soc.connect(server_addr)
    print(f"[*] Successfully connected to the server ...")

    try:
        while True:
            time.sleep(2)
            
            user_input = input()

            if user_input.lower() == "g":
                print("\033[91m{}\033[0m".format("Receiving ...."))
                # Receive the response from the server
                recv_data = client_soc.recv(1024)
                print(f"[*] Received data: {recv_data.decode('utf-8')}")

            elif user_input.lower() == "d":
                data = input("\033[91m{}\033[0m".format("Enter the data to send (or type 'exit' to quit): ")) or "N/A"
                if data.lower() == "exit":
                    break
                # Send data to the server
                client_soc.sendall(data.encode('utf-8'))
            
            elif user_input.lower() == "exit":
                break

    finally:
        client_soc.close()

if __name__ == "__main__":
    host = "server addr"
    port = 8080
    client(host, port)
