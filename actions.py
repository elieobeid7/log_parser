import smtplib
from constants import FROM_EMAIL, TO_EMAIL, EMAIL_SERVER_HOST, EMAIL_MESSAGE


def sendEmail(message):
    msg = ''.join((EMAIL_MESSAGE, message))
    server = smtplib.SMTP(EMAIL_SERVER_HOST)
    server.sendmail(FROM_EMAIL, TO_EMAIL, msg)
    server.quit()