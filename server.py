from flask import Flask, request, jsonify
import smtplib

app = Flask(__name__)

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("cs198199wsg@gmail.com", "p4ssw0rd123.")

msg = "Yehey!"
server.sendmail("cs198199wsg@gmail.com", "dccaingat@up.edu.ph", msg)
server.quit()


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
