"""Portable local launcher. Python 3.11+; first run installs pinned dependencies."""
import argparse
import os
import socket
from pathlib import Path
import subprocess
import sys
import threading
import venv
import webbrowser

ROOT=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser(description='Jalankan Project Nura di komputer ini.')
    parser.add_argument('--port',type=int,default=5000)
    parser.add_argument('--no-browser',action='store_true')
    args=parser.parse_args()
    if sys.version_info<(3,11):raise SystemExit('Project Nura memerlukan Python 3.11 atau lebih baru.')
    if not 1024<=args.port<=65535:raise SystemExit('Pilih port 1024–65535.')
    folder=ROOT/'.venv';python=folder/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
    if not python.exists():
        print('Menyiapkan lingkungan Python lokal…',flush=True)
        venv.EnvBuilder(with_pip=True).create(folder)
    requirements=ROOT/'requirements.txt';marker=folder/'nura-requirements.txt'
    if not marker.exists() or marker.read_bytes()!=requirements.read_bytes():
        print('Memasang dependensi. Internet diperlukan pada pemasangan pertama…',flush=True)
        subprocess.run([str(python),'-m','pip','install','--disable-pip-version-check','-r',str(requirements)],check=True,cwd=ROOT)
        marker.write_bytes(requirements.read_bytes())
    with socket.socket() as connection:
        if connection.connect_ex(('127.0.0.1',args.port))==0:
            raise SystemExit(f'Port {args.port} sedang dipakai. Tutup server lama atau pilih --port 5050.')
    address=f'http://127.0.0.1:{args.port}'
    print('\nProject Nura: '+address+'\nDatabase: instance/nura.sqlite3 (atau NURA_DB_PATH)\nTekan Ctrl+C untuk menghentikan server.\n',flush=True)
    if not args.no_browser:
        timer=threading.Timer(1.5,lambda:webbrowser.open(address));timer.daemon=True;timer.start()
    try:return subprocess.call([str(python),str(ROOT/'app.py'),'--port',str(args.port)],cwd=ROOT)
    except KeyboardInterrupt:return 0

if __name__=='__main__':raise SystemExit(main())
