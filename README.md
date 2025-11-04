# TCP Socket Programming and Packet Capture  

This project explores **TCP socket programming** in Python by building a simple client–server application that exchanges messages over a network.  
It also includes **packet capture and analysis** using Wireshark to visualize how data travels between the two endpoints.  

This was developed as part of my *Computer Networking* coursework at Rutgers University.  

---

## Overview  
The goal of this project was to gain hands-on experience with Python’s `socket` module, understand how TCP connections are established, and analyze packet behavior at the transport layer.  

Two programs were implemented:
- **server.py** – Listens for incoming client connections and echoes messages back.  
- **client.py** – Connects to the server and sends text messages through a TCP socket.  

Using **Wireshark**, I captured packet traffic between the client and server to study TCP handshakes, acknowledgments, and message delivery.

---

## Key Concepts  
- TCP socket creation and binding  
- Establishing connections using `connect()` and `accept()`  
- Sending and receiving data with `send()` and `recv()`  
- Multi-threaded communication for concurrent message handling  
- Packet analysis and interpretation with Wireshark  

---

## Technologies Used  
- **Python 3**  
- **Wireshark**  
- **TCP/IP Protocol Suite**

---

## Project Structure  
- client.py # Client-side socket program
- server.py # Server-side socket program
- proj1_part1.pcap # Wireshark packet capture (part 1)
- proj1_part2.pcap # Wireshark packet capture (part 2)

---

## How to Run  
1. Start the server in one terminal:  
   ```bash
   python3 server.py

2. Run the client in another terminal:
   ```bash
   python3 client.py

4. Type messages into the client — the server will echo them back.

5. Open Wireshark to monitor the TCP packets during communication.
