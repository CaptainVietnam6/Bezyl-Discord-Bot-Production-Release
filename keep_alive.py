#this code is so uptimerobot or an external server can refresh this page and keep the bot online
#will no longer be required as repl will be boosted and kept online 24/7

#important imports for system
import flask
import threading
from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def home():
    return "Bezyl is online and active"

def run():
    app.run(host = "0.0.0.0", port = 8080)

def keep_alive():
    t = Thread(target = run)
    t.start()
