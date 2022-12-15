import json
import os

from smtplib import SMTP_SSL
from email.mime.text import MIMEText

from zzxbot import ZZX_CONFIG


config_file = os.path.join(ZZX_CONFIG, "email.json")
if not os.path.isfile(config_file):
    with open(config_file, "w", encoding="utf-8") as f:
        f.write('{"smtpserver": "", "sender": "", "mail_password": ""}')

with open(config_file, "r", encoding="utf-8") as f:
    config: dict = json.load(f)

smtpserver = config["smtpserver"]
sender: str = config["sender"]
mail_password = config["mail_password"]


def send_email(title: str, message: str, receiver: str, message_type: str = 'plain'):
    msg = MIMEText(message, message_type, _charset="utf-8")
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = title
    with SMTP_SSL(host=smtpserver, port=465) as smtp:
        smtp.login(sender.split("@")[0], mail_password)
        smtp.sendmail(from_addr=sender, to_addrs=[
                      receiver], msg=msg.as_string())
