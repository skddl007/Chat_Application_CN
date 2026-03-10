-- Chat Application using TCP Sockets

This project is a simple multi-client chat application developed using Python socket programming. The application consists of a server and multiple clients. The server handles all connections and message transfers, while the clients connect to the server to send and receive messages.

The goal of this project is to understand how TCP communication works and how multiple users can communicate through a centralized server using sockets and threads.

-- Working of the Application

The chat system works on a client–server model. The server first starts and waits for client connections on a specific port. When a client connects, the server assigns a separate thread to handle that client so that multiple users can communicate at the same time.

Each client joins the chat by entering a username. When a user sends a message, the server receives it and broadcasts it to all other connected clients. If a user leaves the chat, the server informs the remaining users and removes that client from the active list.

Because the application uses TCP sockets, the messages are delivered reliably and in the correct order.

-- Project Files

The project is divided into two main parts:

-- Server

server.py – runs the chat server and manages client connections

chat_history.txt – stores chat messages with timestamps

server_log.txt – records server events such as client connections and joins

-- Client

client.py – connects to the server and allows users to send and receive messages

-- Running the Project

Start the server by running:

python Server/server.py

Open another terminal and start the client:

python Client/client.py

Enter a username.

Multiple clients can be started in different terminals to simulate a group chat.

-- Client Commands

Send message: type the message and press Enter

/quit – exit the chat

/users – display the list of connected users

-- Logging

The server maintains two files:

Chat History – stores all messages with timestamps.

Server Log – records events such as server start, client connection, and user join/leave.

Testing

The application was tested with multiple clients joining the chat simultaneously. Messages were successfully broadcast to all connected users. Client disconnections were handled correctly, and the server remained stable during testing. The screenshots included in the report show these test results.

Limitation

Currently the server runs on 0.0.0.0:8000 and the client connects to 127.0.0.1:8000. To run the application on different machines, the client IP must be changed to the server machine’s IP address.

