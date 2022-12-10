from socket import socket
from threading import Thread

from game2 import Game
from player2 import Player


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket()
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        self.connections = []
        self.threads = []
        self.running = True
        self.players = []
        self.games = []

    def start(self):
        while self.running:
            print("SERVER: Waiting for connections...")
            conn, addr = self.socket.accept()
            print("SERVER: Connection from: " + str(addr))
            self.connections.append(conn)
            thread = Thread(target=self.handle, args=(conn, addr))
            self.threads.append(thread)
            thread.start()

    def handle(self, conn, addr):
        try:
            while self.running:
                # TODO: Handle client request
                if conn.recv(1024).decode() == 'start':
                    conn.send(b'username ?')
                    username = conn.recv(2048).decode()
                    player = Player(username, conn, addr)
                    self.players.append(player)

                    if len(self.connections) == 2:
                        player.connection.send('X or O ?'.encode())
                        player.button = player.connection.recv(2048).decode()
                        game = Game('localhost',self.players[0],self.players[1])
                        self.games.append(game)
                        player.connection.send(b'welcome ' + player.name.encode())
                        while True:
                            self.games[0].hand(self.players[0], self.players[1])


        except Exception as e:
            print(e)
            print("SERVER: Connection closed: " + str(addr))
            self.connections.remove(conn)
            self.threads.remove(Thread(target=self.handle, args=(conn, addr)))
            conn.close()

     




    def stop(self):
        self.running = False
        for conn in self.connections:
            conn.close()
        for thread in self.threads:
            thread.join()
        self.socket.close()

    def send_all(self, data):
        for conn in self.connections:
            conn.send(data)

    def get_connections(self):
        return self.connections
    def get_game(self):
        return self.games[0]    
