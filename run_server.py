import subprocess
from app.core.globals import globals

IP = globals.IP
PORT = globals.PORT

def start_server(IP: str, PORT: str):
    subprocess.run(["uvicorn", "app.main:app", "--host", IP, "--port", PORT, "--reload"])

if __name__ == "__main__":
    start_server(IP, PORT)
