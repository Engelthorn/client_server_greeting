#!/usr/bin/python3.12
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread


def handle_client(tcp_client_socket):
    """Get message from Client and send greeting as respond to Client."""
    request = tcp_client_socket.recv(1024)
    print(f"\t[+] Received from TCP Client: {request.decode('utf-8')}")
    tcp_client_socket.send("\t[TCP SERVER] Hello from CNC!".encode())


def run(ip_addr='', port=7777):
    """Run Multi-Server. Bind port - 7777. Supports 5 connections."""
    try:
        tcp_server = socket(AF_INET, SOCK_STREAM)
        tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        tcp_server.bind((ip_addr, port))
        tcp_server.listen(5)
        print("\n-------------------------------------------------------"
              "\n[!] CNC is listening for incoming connections..."
              "\n[!] Press CTRL + C to stop CNC.")

        while True:
            client_connection, client_ip = tcp_server.accept()
            print(f"\n\t[+] Get connection from {client_ip[0]}:{client_ip[1]}")

            client_handler = Thread(target=handle_client, args=(client_connection,))
            client_handler.start()

    except KeyboardInterrupt:
        print("\n[+] You have stopped CNC!"
              "\n-------------------------------------------------------")


run()
