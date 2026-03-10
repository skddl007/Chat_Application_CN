Simple Chat Application using TCP Sockets

This project is a basic multi-client chat application created using Python and TCP sockets.
A central server manages the communication, and multiple clients can connect to it at the same time. When a user sends a message, the server receives it and forwards it to all other connected clients.

The goal of this project is to demonstrate how socket programming can be used to build a simple real-time communication system.

Main Features

Multiple Clients Support
The server can handle several clients at the same time. It listens for incoming connections and creates a separate thread for each connected client.

Usernames and Join/Leave Messages
When a client joins the chat, they provide a username. The server informs all other users when someone joins or leaves the chat.

Message Broadcasting
Any message sent by a client is received by the server and then forwarded to all other connected clients.

Handling Client Disconnects
If a user exits the chat or their connection drops, the server removes that user from the active list and informs other users.

Reliable Communication
Since the system uses TCP sockets, messages are delivered reliably and in order.

Project Structure

The project is organized into two main folders:

Server

server.py – runs the chat server and manages all clients

chat_history.txt – stores chat messages with timestamps

server_log.txt – records server activities such as connections and disconnections

Client

client.py – connects to the server and allows users to send and receive messages

Requirements

Python 3.x

Only Python’s standard library is used (no external packages are required)

How to Run the Application
Start the Server

Run the following command from the project directory:

python Server/server.py

The server will start running on port 8000 and will wait for clients to connect.

Start the Client

Open a new terminal window and run:

python Client/client.py

Enter a username when prompted.
You can open multiple terminals and start multiple clients to simulate a group chat.

If a username is already in use, the server will reject it and the user must reconnect with a different name.

Client Commands

Inside the chat client:

Send a message: simply type the message and press Enter

Exit the chat: type /quit

View connected users: type /users

Communication Protocol

The client and server communicate using simple text messages over TCP.
Some of the commands used between the client and server are:

JOIN <username> – used when a client connects

MSG <message> – used to send a chat message

USERS – request the list of connected users

QUIT – leave the chat

Example messages exchanged between client and server:

JOIN Sandeep
MSG Hello everyone!
USERS
QUIT
Concurrency Design

The application uses multithreading.

Server Side
The server continuously listens for new connections.
When a client connects, a new thread is created to handle communication with that client.

Client Side
The client also uses two threads:

one thread listens for incoming messages from the server

the main thread reads user input and sends messages

This design allows users to send and receive messages at the same time.

Logging and Chat History

The server stores useful information in two files.

Chat History

All chat messages are saved with timestamps.

Example:

[23:04:55] [23:04] Sandeep: Are you Happy😊
[23:15:05] [23:15] Shivam: I think you feel happy😊
[23:16:14] [23:16] Shivam: Its thoughtful game🧠

Server Logs

Server events such as connections and joins are also recorded.

Example:

[22:38:29] Chat server started on Port 8000
[22:39:37] Client Connected: ('127.0.0.1', 12732)
[22:39:37] ## Sandeep joined the chat ##
[22:40:06] Client Connected: ('127.0.0.1', 8959)
[22:40:06] ## Gaurav joined the chat ##
Testing Performed

The application was tested under several conditions:

Multiple clients connecting to the server

Messages sent from different clients at the same time

Clients leaving the chat normally using /quit

Clients disconnecting unexpectedly

Sending empty messages or very long messages

All these cases worked correctly and the server remained stable during testing.
The screenshots included in the report show the results of these tests clearly.

Limitations

Currently the application uses fixed addresses:

Server: 0.0.0.0:8000

Client: 127.0.0.1:8000

To run the chat between different machines, the client must use the server machine’s IP address.

Also, messages are read using recv(1024), so extremely long messages could be split at the TCP level.
