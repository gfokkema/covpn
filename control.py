import os
import select
import socket
import sys

def listen(client):
    quit = False
    while not quit:
        try:
            rsock, wsock, esock = select.select([sys.stdin, client], [], [])
            for sock in rsock:
                if sock == client:
                    msg = sock.recv(4096)
                    sys.stdout.write(msg.decode('utf-8'))
                if sock == sys.stdin:
                    msg = sys.stdin.readline()
                    client.send(msg.encode('utf-8'))
            sys.stdout.write('> ')
            sys.stdout.flush()
        except KeyboardInterrupt as k:
            quit = True

def main():
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.connect('/run/openvpn.sock')
        listen(client)

if __name__ == '__main__':
    main()
