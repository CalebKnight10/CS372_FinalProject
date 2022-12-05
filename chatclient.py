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
        "nickname": nickname
    }
	contents = json.dumps(contents)

	return contents


# Need to get the clients chat payload
def clientsChatPayload(contents):
    client_chat_payload = {
    "type": "chat",
    "contents": contents
    }
    contents = json.dumps(client_chat_payload)

    return contents


def contentsOfPacket(contents):
	if contents['type'] == 'join':
		payload = (f"*** {contents['nickname']} joined the chat")
		return payload
	if contents['type'] == 'chat':
		payload = (f"{contents['nickname']} {contents['contents']}")
		return (payload)
	else:
		payload = (f"*** {contents['nickname']} left the chat")
		return payload


def serverContents(s):
	while True:
		contents = s.recv(4096).decode()
		contents = json.loads(contents)
		print_message(contentsOfPacket(contents))


def userInput(nickname, s):
	while True:
		# contents = read_command(f"{nickname}>  ")
		contents = read_command(nickname + "> ")
		print_message(f"{nickname}: {contents}")
		if contents.startswith('/q'):
			sys.exit()
			s.close()
		elif len(contents) == 0:
			continue
		else:
			s.send(clientsChatPayload(contents).encode())

def thread(s):
	threads = [threading.Thread(target=serverContents(s), args=(s,), daemon=True), threading.Thread(target=serverContents(s), args=(s, nickname))]
	for t in threads:
		t.start()
	threads[1].join()

	return threads


def main(argv):
	nickname = argv[1]
	port = int(argv[2])
	host = argv[3]

	init_windows()

	# Connect to socket
	s = socket.socket()
	s.connect((host, port))

	hello_message = helloPayload(nickname).encode()
	s.send(hello_message)

	thread(s)

	end_windows()

	s.close()


if __name__ == "__main__":
    sys.exit(main(sys.argv))


