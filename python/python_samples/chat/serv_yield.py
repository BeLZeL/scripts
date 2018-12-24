#!/usr/bin/env python3
# https://connect.ed-diamond.com/GNU-Linux-Magazine/GLMF-219/Le-cerveau-de-Peter
# server : ./serv.py
# clients : telnet 127.0.0.1 5555

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

def conn_sock_manager(conn_s):
    conn_sockets.append(conn_s)
    line = b''
    while True:
        yield conn_s
        c = conn_s.recv(1)
        if c == b'':
            break
        line += c
        if c == b'\n':
            send_line(conn_s, line)
            line = b''
    conn_s.close()
    conn_sockets.remove(conn_s)

def server_sock_manager():
    s = create_server_sock()
    while True:
        yield s
        conn_s, addr = s.accept()
        scheduler.start_generator(conn_sock_manager(conn_s))

class Scheduler:
    def __init__(self):
        self.socks = {}

    def run(self):
        while True:
            generator = self.wait()
            self.step_generator(generator)

    def wait(self):
        socks = list(self.socks.keys())
        r, w, e = select(socks, [], [])
        sock = r[0]
        generator = self.socks.pop(sock)
        return generator
    
    def step_generator(self, generator):
        try:
            # run the generator up to the next yield
            sock = generator.__next__()
        except StopIteration:
            return # end of generator
        # save the fact that generator is now waiting on sock
        self.socks[sock] = generator

    def start_generator(self, generator):
        self.step_generator(generator) # start = run 1st step

scheduler = Scheduler()
scheduler.start_generator(server_sock_manager())
scheduler.run()
