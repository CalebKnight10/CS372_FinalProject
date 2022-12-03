import sys
import socket
import threading
import json
import select




# Have dict/set for sockets/buffers



# Handle listener socket




# Connect socket
# Make the server socket and bind it to the port
servers_socket = socket.socket()
servers_socket.bind(("", port))
servers_socket.liste
# listener socket
listener = [servers_socket]



# If socket is listener, accept

# Else, recv data if no data close




# Get the servers chat payload
def get_server_chat_payload(nickname, chat):
    server_chat = {
    "type": "chat",
    "nick": nickname,
    "message": chat
    }
    return json.dumps(server_chat)


# Get the join and the leave payload
def get_join_payload(name_of_joinee):
    join = {
    "type": "join",
    "nick": name_of_joinee
    }
    return json.dumps(join)

def get_leave_payload(name_of_leaver):
    leave = {
    "type": "leave",
    "nick": name_of_leaver
    }
    return json.dumps(leave)

