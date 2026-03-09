# Simple Chat Application (TCP Sockets)

Multi-client chat application built with **Python TCP sockets**. It uses a **central server** that accepts multiple clients concurrently and **broadcasts** chat messages to all connected users.

## Features (mapped to assignment requirements)

- **Multi-client server (10+ clients)**: Server listens with a backlog of `10` and spawns a thread per client.
- **Usernames + join/leave notifications**: Clients send `JOIN <username>`; server broadcasts join/leave events.
- **Broadcast messaging**: `MSG <text>` from one client is delivered to all other connected clients.
- **Graceful disconnect handling**: Server removes users on `QUIT` or unexpected disconnect.
- **Reliable, ordered delivery**: Uses TCP.

## Project structure

- `Server/server.py`: Chat server (thread-per-client).
- `Client/client.py`: Chat client (one thread for receiving + main thread for sending).
- `Server/chat_history.txt`: Persisted chat messages (created/updated by server).
- `Server/server_log.txt`: Server event log (created/updated by server).

## Requirements

- Python 3.x
- No external libraries (standard library only)

## How to run

### 1) Start the server

From the project root:

```bash
python Server/server.py
```

The server binds to `0.0.0.0:8000` (all interfaces) and runs until you stop it (Ctrl+C / close terminal).

### 2) Start one or more clients

Open **multiple terminals** and run:

```bash
python Client/client.py
```

Enter a username when prompted. If a username is already taken, the server replies with `Username is already taken.` (choose another and reconnect).

## Client commands

- **Send a chat message**: type anything and press Enter
- **Quit**: `/quit` (client sends `QUIT` and exits)
- **List users**: `/users` (client sends `USERS` and prints the server response)

## Application-layer protocol

Messages are plain UTF-8 text over TCP.

- `JOIN <username>`
- `MSG <message text>`
- `QUIT`
- `USERS` 

### Example exchange

- Client → Server: `JOIN Sandeep`
- Client → Server: `MSG Hello everyone!`
- Client → Server: `USERS`
- Client → Server: `QUIT`

## Concurrency design

- **Server**: accepts connections in a loop and starts a **dedicated thread per client** (`threading.Thread`) to handle receive/parse/broadcast.
- **Client**: runs a **receiver thread** to print messages in real time while the main thread reads user input and sends messages.

## Logging / persistence (extra credit)

- **Chat history**: server appends messages to `Server/chat_history.txt` with timestamps.
- **Server events**: server appends join/leave/start events to `Server/server_log.txt` with timestamps.

## Testing checklist (as required)

- **Multiple clients joining**: start 3+ clients with different usernames.
- **Simultaneous messaging**: type messages in different clients quickly; all others should receive them.
- **Client disconnection**: use `/quit` and also test closing a client terminal unexpectedly.
- **Server stability**: keep server running while clients come/go.
- **Edge cases**:
  - empty message (client blocks it)
  - long message \(> 300 chars\) (client blocks it)

## Notes / known limitations

- Server/client currently use a **fixed host/port**:
  - server: `0.0.0.0:8000`
  - client: `127.0.0.1:8000`
  To chat across multiple machines, update the client IP to the server machine’s LAN IP.
- Messages are read using `recv(1024)`, so extremely long single messages could be split at the TCP level (typical for simple assignments).