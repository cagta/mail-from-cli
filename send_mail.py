import sys, os
import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.generator import Generator

from io import StringIO

msg = MIMEMultipart()
msg['From'] = os.environ.get("FROM")

hasAttachment = 0

if (len(sys.argv) == 2):
    sendto = os.environ.get("TO_KINDLE")
    msg['Subject'] = "convert"
    body = "Automatically send by send-mail"
    hasAttachment = 1
else:
    sendto = sys.argv[1]
    msg['Subject'] = sys.argv[2]
    body = sys.argv[3]
    if len(sys.argv) > 4:
        hasAttachment = 4

msg['To'] = sendto
msg.attach(MIMEText(body))

if hasAttachment != 0:
    with open(sys.argv[hasAttachment], "rb") as fil:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(fil.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', 'attachment', filename=sys.argv[hasAttachment])
    msg.attach(attachment)

# convert MIME message to string
fp = StringIO()
gen = Generator(fp, mangle_from_=False)
gen.flatten(msg)
msg = fp.getvalue()

mailserver = smtplib.SMTP(os.environ.get("SMTP_HOST"),os.environ.get("SMTP_PORT"))
mailserver.login(os.environ.get("FROM"), os.environ.get("SMTP_PASS"))
mailserver.sendmail(os.environ.get("FROM"),sendto,msg)
mailserver.quit()