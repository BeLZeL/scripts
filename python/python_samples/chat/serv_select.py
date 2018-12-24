#!/usr/bin/env python3
# https://connect.ed-diamond.com/GNU-Linux-Magazine/GLMF-219/Le-cerveau-de-Peter
# server : ./serv.py
# clients : telnet 127.0.0.1 5555


#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from select import select

conn_sockets = []

def send_line(sender, line):
    for recv_s in conn_sockets:
        if recv_s != sender:
            recv_s.send(line)

def create_server_sock():
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('', 5555))
    s.listen(0)
    return s

def conn_sock_readline(conn_s):
    line = b''
    while True:
        c = conn_s.recv(1)
        if c == b'': # disconnected
            conn_s.close()
            conn_sockets.remove(conn_s)
            break
        line += c
        if c == b'\n': # end-of-line
            send_line(conn_s, line)
            break

def main():
    server_sock = create_server_sock()
    while True:
        fds = tuple(conn_sockets) + (server_sock,)
        r, w, e = select(fds, [], [])
        fd = r[0]
        if fd == server_sock:
            conn_s, addr = server_sock.accept()
            conn_sockets.append(conn_s)
        else:
            conn_sock_readline(fd)

main()
