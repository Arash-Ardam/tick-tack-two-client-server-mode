from client2 import Client
from constants2 import *


def __main__():
    client = Client(SERVER_HOST, SERVER_PORT)
    while True:
        print("***************\n"
              "1. Connect to server\n"
              "2. Exit\n"
              "***************")
        choice = input("Enter your choice: ")
        if choice == "1":
            client.start()
        elif choice == "2":
            client.stop()
            break


if __name__ == "__main__":
    __main__()
