import smtplib
import schedule
import time

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    message = 'Subject: Automated Email\n\nThis is an automated email.'
    server.sendmail('your_email@gmail.com', 'recipient_email@gmail.com', message)
    server.quit()

# Scheduling to run every day at a specific time
schedule.every().day.at("09:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait a minute between checks