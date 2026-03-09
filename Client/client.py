import socket
import threading


#recieve msg from server
def recv_msg(sock):
    while True:
        try:
            msg = sock.recv(1024).decode("utf-8")
            if not msg:
                break
            print(msg)
        
        except:
            break


#send msg to server
def send_msg(sock):
    while True:
        msg = input()
        
        # Handle empty message
        if msg.strip() == "":
            print("Empty message can not send")
            continue

        # Handle very long message
        if len(msg) > 300:
            print("Message limit is 300 char")
            continue
        
        #Exit command
        if msg == "/quit":
            sock.send("QUIT".encode("utf-8"))
            
            sock.close()
            break
        
        # users command
        elif msg == "/users":
            sock.send("USERS".encode("utf-8"))
        
        else:
            formatted_msg = "MSG " + msg
            sock.send(formatted_msg.encode("utf-8"))


def start_client():
    
    username = input("enter username:-")
    
    client_sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #Address Family use IPv4 and use TCP
    client_sckt.connect(("127.0.0.1", 8000))
    
    #JOIN cmd
    join_msg = "JOIN " + username
    
    client_sckt.send(join_msg.encode("utf-8"))
    
    #start recieving thread
    recv_thread = threading.Thread(target = recv_msg,args=(client_sckt,))
    recv_thread.start()
    
    #start send msg
    send_msg(client_sckt)


if __name__ == "__main__":
    start_client()
