from server2 import Server
from threading import Thread
from constants2 import *


def __main__():
    server = Server(HOST, PORT_NUMBER)
    thread = Thread(target=server.start)
    while True:
        print("***************\n"
              "1. Start server\n"
              "2. Get list of running games\n"
              "3. Stop server\n"
              "***************")
        choice = input("Enter your choice: ")
        if choice == "1":
            thread.start()
        elif choice == "3":

            pass
        elif choice == "2":
            print(server.get_game())
            # TODO: Get list of running games
            pass


if __name__ == "__main__":
    __main__()
