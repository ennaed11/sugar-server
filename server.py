from flask import Flask, request, jsonify
import smtplib
from mailer import Mailer

app = Flask(__name__)

MAIL_USERNAME = 'cs198199wsg@gmail.com'
MAIL_PASS = 'p4ssw0rd123.'
MAIL_URL = 'smtp.gmail.com'
MAIL_PORT = 587

mailer = Mailer(MAIL_USERNAME, MAIL_PASS, MAIL_URL, MAIL_PORT)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/logs', methods=['POST'])
def parseLogs():
    data = request.json
    print(data)

    # do something with data

    return jsonify({"success": True})

app.run()
