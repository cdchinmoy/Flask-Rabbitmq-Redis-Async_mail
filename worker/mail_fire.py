from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message
import smtplib

# create message object instance
msg = MIMEMultipart()
password = "Chinmoy123!@#"

def send_mail(recevier, subject, body):
    msg = email.message.Message()
    msg['From'] = "chinmoy.ogmait@gmail.com"
    msg['To'] = recevier
    msg['Subject'] = subject

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
    
    print("successfully sent email")

# recever,subject,body = "cdchinmoy@gmail.com","Hello World","<h1>Hello World!</h1>"
# send_mail(recever,subject,body)  