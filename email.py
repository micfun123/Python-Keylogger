import email
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email():
        
    email_adress = os.environ.get("EMAIL")
    app_password = os.environ.get("APP_PASSWORD")

    subject = "Log File"
    body = "Log File"
    sender_email = email_adress
    receiver_email = email_adress
    password = app_password

    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject
    #attach the log file
    filename = "log.txt"
    attachment = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={filename}")
    email.attach(part)
    text = email.as_string()
    #send the email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    server.quit()


