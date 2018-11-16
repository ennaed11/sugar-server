from flask import Flask, request, jsonify
import smtplib
from mailer import Mailer
import csv

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

    filename = 'blood.csv'
    with open(filename, 'w+') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['value', 'startDate', 'endDate'])
        for item in data['blood']:
            writer.writerow([item['value'], item['startDate'], item['endDate']])
        
        text = 'Date of Birth: {}\nAge: {}'.format(data['dob']['value'], data['dob']['age'])
        mailer.sendMessage(['dccaingat@up.edu.ph', 'mfmayol@up.edu.ph'], 'Blood Sugar Report', text, [filename])

        return jsonify({"success": True})

app.run(debug=True)
