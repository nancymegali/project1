#!/usr/bin/env python3
import argparse, socket
from pathlib import Path

def main():
    p = argparse.ArgumentParser(description="CS352 Project 1 client")
    p.add_argument("--server-host", required=True)
    p.add_argument("--server-port", type=int, required=True)
    p.add_argument("--infile", default="in-proj.txt")
    p.add_argument("--outfile", default="out-proj.txt")
    a = p.parse_args()

    in_path, out_path = Path(a.infile), Path(a.outfile)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((a.server_host, a.server_port))
        rfile = s.makefile("r", encoding="utf-8", newline="\n")
        wfile = s.makefile("w", encoding="utf-8", newline="\n", buffering=1)

        welcome = rfile.readline().rstrip("\n")
        print(f"[C] From server: {welcome}")

        lines = in_path.read_text(encoding="utf-8").splitlines()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as out_f:
            for line in lines:
                print(f"[C] Sending: {line}")
                wfile.write(line + "\n"); wfile.flush()
                reply = rfile.readline().rstrip("\n")
                print(f"[C] Reply:   {reply}")
                out_f.write(reply + "\n")

        wfile.flush(); wfile.close(); rfile.close()

if __name__ == "__main__":
    main()
