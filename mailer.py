from smtplib import SMTP
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

class Mailer:
    def __init__(self, username, password, url, port):
        self.username = username
        self.password = password
        self.url = url
        self.port = port
    
    def sendMail(self, send_to, msg):
        server = SMTP(url, port)
        server = SMTP(url, port)
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.username, send_to, msg)
        server.close()
    
    def createMessage(self, send_to, subject, text):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime = True)
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        return msg
    
    def sendMessage(self, send_to, subject, text, files = None):
        assert isinstance(send_to, list)

        msg = self.createMessage(COMMASPACE.join(send_to), subject, text)

        for f in files or []:
            with open(f, "rb") as f:
                part = MIMEApplication(f.read(), Name=basename(f))
            part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(f))
            msg.attach(part)
        
        self.sendMail(send_to, msg.as_string())