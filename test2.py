# Checking the certificate 

from urllib.request import ssl, socket
import datetime, smtplib
hostname = 'nihitjain.me'
port = '443'
context = ssl.create_default_context()
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname = hostname) as ssock:
        certificate = ssock.getpeercert()
# print (certificate)
# Validating the Expiration Date

certExpires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')

daysToExpiration = (certExpires - datetime.datetime.now()).days

if daysToExpiration == 39 or daysToExpiration == 10:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('abhisheksaini7029@gmail.com','bicdfeyuugoaypuv')
    server.sendmail('abhisheksaini7029@gmail.com','pankaj@tothenew.com','Your certificate is about to expire in 39 days - pelase renew it ')

    # send_notification(daysToExpiration)
# print (daysToExpiration)
# Creating the Notification Action

# def send_notification(days_to_expire):
#     smtp_port = 587
#     smtp_server = "smtp.acmecorp.com"
#     sender_email = "abhisheksaini7029@gmail.com"
#     receiver_email = "abhishek1@tothenew"
#     password = "bicdfeyuugoaypuv"
#     if days_to_expire== 30:
#         days = "1 day"
#     else:
#         days = str(days_to_expire) + " days"
#     message = """\
#         Subject: Certificate Expiration
#         The TLS Certificate for your site expires in {days}"""
#     email_context = ssl.create_default_context()
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls(context = email_context)
#         server.login(sender_email, password)
#         server.sendmail(sender_email, 
#                         receiver_email, 
#                         message.format(days = days))