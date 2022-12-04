# Caleb Knight
# CS 372 Final Project
# A client chat server


import sys
import socket
import threading
import json
import select


# Get the servers chat payload
def getServerChatPayload(nickname, chat):
    server_chat = {
    "type": "chat",
    "nick": nickname,
    "message": chat
    }
    return json.dumps(server_chat)


# Get the join and the leave payload
def getJoinPayload(name_of_joinee):
    join = {
    "type": "join",
    "nick": name_of_joinee
    }
    return json.dumps(join)

def getLeavePayload(name_of_leaver):
    leave = {
    "type": "leave",
    "nick": name_of_leaver
    }
    return json.dumps(leave)



def runServer(port):
	# Have dict/set for sockets/buffers
    client_buffers = {}

    # Make the server socket and bind it to the port
    servers_socket = socket.socket()
    servers_socket.bind(("", port))
    servers_socket.listen()

    # listener socket
    listener = [servers_socket]

    # loop forever
    while True:

        # call select(), get sockets that are ready-to-read
        ready_to_read, _, _ = select.select(listener, [], [])

        # for each socket that is ready-to-read
        for s in ready_to_read:

            # if the socket is the listener socket, then accept the connection
            if s is servers_socket:
                clients_socket, _ = servers_socket.accept()
                listener.append(clients_socket)

            # else it is just a regular socket
            else:
                contents = s.recv(4096)

                # if no content, client disconnected
                if not contents:
                    print_client_disconnection(s)
                    s.close()
                    listener.remove(s)
                    client = client_buffers.pop(s)
                    getLeavePayload(client)
                    print(f"*** {client} left the chat")
                else:
                	for c in contents.decode():
                		if re.search('join', c):
                			joinPacket(s, contents, client_buffers)
                		else:
                			chatPacket(s, contents, client_buffers)



def joinPacket(s, contents, client_buffers): 
	contents = contents.decode()

	join_packet = json.load(contents)
	print(f"*** {join_packet['nickname']} joined the chat")
	client_buffers[s] = join_packet['nickname']
	getJoinPayload(join_packet['nickname'])


def chatPacket(s, contents, client_buffers):
	contents = contents.decode()

	chat_packet = json.load(contents)

	print(f"*** {join_packet['nickname']} joined the chat")
	client_buffers[s] = join_packet['nickname']
	getServerChatPayload(join_packet['nickname'])

def main(argv):

	port = int(argv[1])

	runServer(port)




if __name__ == "__main__":
    sys.exit(main(sys.argv))