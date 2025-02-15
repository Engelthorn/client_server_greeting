#!/usr/bin/python3.12
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv


def run(server_ip=argv[1], port=7777):
    """Specify Server's IP than run. Bind port - 7777."""
    try:
        tcp_client = socket(AF_INET, SOCK_STREAM)
        tcp_client.connect((server_ip, port))
        tcp_client.send("Hello from TCP Client!".encode())

        server_response = tcp_client.recv(4064).decode()
        print(server_response)

        tcp_client.close()

    except ConnectionRefusedError:
        print("\n[-] Server is OFFLINE!"
              "\n------------------------------------------------")

    except IndexError:
        print("\n[!] Specify Server's IP address!"
              "\n------------------------------------------------")


run()
