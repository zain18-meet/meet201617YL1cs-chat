# Server for turtle_chat
import sys, socket, select

DEFAULT_HOST = 'localhost'
SOCKET_LIST = []
RECV_BUFFER = 4096 
DEFAULT_PORT = 9009

def chat_server(HOST=DEFAULT_HOST, PORT=DEFAULT_PORT):
    '''
    Run this method in main to spawn a new server.

    :param HOST: hostname, string.  Default='localhost'.
    :param PORT: port number, integer.  Default=9009
    '''
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
 
    print("Chat server started on port " + str(PORT))
 
    while True:

        # get the list of sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            # a new connection request recieved
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print("Client (%s, %s) connected" % addr)
                broadcast(server_socket, sockfd, "Client (%s, %s) entered our chat session\n" % addr)

            # a message from a client, not a new connection
            else:
                # process data recieved from client, 
                # receiving data from the socket.
                data = sock.recv(RECV_BUFFER)
                if data:
                    print(data.decode())
                    # there is something in the socket
                    #Need to decode data to combine with string
                    #broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data.decode())  
                    broadcast(server_socket, sock, data.decode())  
                else:
                    # remove the socket that's broken    
                    if sock in SOCKET_LIST:
                        SOCKET_LIST.remove(sock)

                    # at this stage, no data means probably the connection has been broken
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

    server_socket.close()
    
# broadcast chat messages to all connected clients
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message.encode())
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
 
if __name__ == "__main__":
    sys.exit(chat_server())


         

