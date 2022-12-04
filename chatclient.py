# Caleb Knight
# CS 372 Final Project
# A client chat server

import sys
import json
import socket
import threading
from chatui import init_windows, read_command, print_message, end_windows


# Need to get the hello payload
def helloPayload(nickname):
	contents = {
        "type": "hello",
        "nick": nickname
    }
	contents = json.dumps(contents)\

	return contents



# Need to get the clients chat payload
def clientsChatPayload(contents):
    client_chat_payload = {
    "type": "chat",
    "message": contents
    }
    contents = json.dumps(client_chat_payload)

    return contents




def contentsOfPacket(contents):
	if contents['type'] == 'join':
		print(f"*** {packet['nickname']} joined the chat")
	if contents['type'] == 'chat':
		print(f"{packet['nickname']} {packet['contents']}")
	else:
		print(f"*** {packet['nickname']} left the chat")

def serverContents(s):
	while True:
		contents = s.recv(4096).decode()
		contents = json.load(contents)
		print_message(contentsOfPacket(contents))

def userInput(nickname, s):
	while True:
		contents = read_command(f"{nickname}>  ")
		print_message(f"{nick}: {contents}")
		if contents[0] == '/q':
			s.close()
		elif len(contents) == 0:
			continue
		else:
			s.sendall(getClientsChatPayload(contents).encode())


def main(argv):
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



