from flask import Flask
from threading import Thread
import os
import subprocess

app = Flask('')


@app.route('/')
def home():
    return 'It is alive'


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


def restart_bot():
    print("===== An error occured - restarting now ====")
    subprocess.call(["sleep", "5", "&&", "python3", "main.py"])
    os.system("kill 1")
    return
