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
    
    def _sendMail(self, send_to, msg):
        server = SMTP(self.url, self.port)
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.username, send_to, msg)
        server.close()
    
    def _createMessage(self, send_to, subject, text):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime = True)
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        return msg
    
    def sendMessage(self, send_to, subject, text, files = None):
        assert isinstance(send_to, list)

        msg = self._createMessage(COMMASPACE.join(send_to), subject, text)

        for f in files or []:
            part = MIMEApplication(open(f, 'rb').read())
            part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(basename(f)))
            msg.attach(part)
        
        self._sendMail(send_to, msg.as_string())