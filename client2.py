from socket import socket


class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket()
        self.running = False

    def start(self):
        self.socket.connect((self.host, self.port))
        self.running = True
        while self.running:
            try:
                # TODO: Add client code here
               
                data = input("Enter data to send: ")
                print("CLIENT: Sending data to server")
                self.socket.send(data.encode())
                data = self.socket.recv(1024)
                print("CLIENT: Received: " + data.decode())
                
            except Exception as e:
                print(e)
                self.running = False
                self.socket.close()

    def stop(self):
        self.running = False
        self.socket.close()

    def send(self, data):
        self.socket.send(data)

    def receive(self):
        return self.socket.recv(1024)
