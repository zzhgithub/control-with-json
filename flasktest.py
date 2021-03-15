from flask import Flask, request

import subprocess
import os

app = Flask(__name__)


@app.route("/run")
def run():
    subprocess.Popen(["python3", "play.py", "test.mp4"], cwd="/Users/zhouzihao/lab/hezi")
    return "ok"


if __name__ == '__main__':
    app.run()
