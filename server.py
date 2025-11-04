#!/usr/bin/env python3
import argparse, socket
from pathlib import Path
WELCOME = b"Welcome to CS 352!\n"

def transform(s: str) -> str:
    return s[::-1].swapcase()

def handle_client(conn: socket.socket, out_path: Path | None):
    conn.sendall(WELCOME)
    buf = b""
    try:
        while True:
            chunk = conn.recv(4096)
            if not chunk: break
            buf += chunk
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                s = line.decode("utf-8", errors="replace").rstrip("\r")
                reply = (transform(s) + "\n").encode("utf-8")
                conn.sendall(reply)
                if out_path:
                    out_path.parent.mkdir(parents=True, exist_ok=True)
                    with out_path.open("a", encoding="utf-8") as f:
                        f.write(reply.decode("utf-8"))
    finally:
        conn.close()

def main():
    p = argparse.ArgumentParser(description="CS352 Project 1 server")
    p.add_argument("--port", type=int, required=True)
    p.add_argument("--host", default="")
    p.add_argument("--log-out", default="out-proj.txt")
    a = p.parse_args()
    out_path = Path(a.log_out) if a.log_out else None
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((a.host, a.port))
        srv.listen(1)
        print(f"[S] Listening on {a.host or '0.0.0.0'}:{a.port}")
        while True:
            conn, addr = srv.accept()
            print(f"[S] Connection from {addr}")
            handle_client(conn, out_path)

if __name__ == "__main__":
    main()
