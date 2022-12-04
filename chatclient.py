# Caleb Knight
# CS 372 Final Project
# A client chat server

import sys
import json
import socket
import threading
from chatui import init_windows, read_command, print_message, end_windows


# Need to get the hello payload
def helloPayload(nick):
	message = {
        "type": "hello",
        "nick": nickname
    }
	message = json.dumps(message)
    
    return message

def userInput(nick):
	while True:
        try:
            command = read_command(f"{nickname}>  ")
        except:
            break
        print_message(f"{nick}: {command}")	


# Need to get the clients chat payload
def getClientsChatPayload(message):
    client_chat_payload = {
    "type": "chat",
    "message": message
    }

    return json.dumps(client_chat_payload)


def main(argv):

    try:
        nickname = argv[1]
        port =int(argv[2])
        host = argv[3]
        
    init_windows()

    # Connect to socket
	s = socket.socket()
    s.connect((host, port))

    hello_message = helloPayload(nick)
    s.sendall(hello_message)


    s.close()


if __name__ == "__main__":
    sys.exit(main(sys.argv))



