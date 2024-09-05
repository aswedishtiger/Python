import smtplib
import os
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# 1: Setting up environment variables for credentials (for security)
# You can set these in your system or use a .env file in real scenarios
EMAIL_ADDRESS = os.getenv('EMAIL_USER', 'your_email@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS', 'your_email_password')

# 2: Function to send an email
def send_email(recipient, subject, body, attachment=None):
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = recipient
        message['Subject'] = subject
        
        # Attach the body message
        message.attach(MIMEText(body, 'plain'))
        
        # Attach a file if provided
        if attachment:
            attach_file = open(attachment, 'rb')
            mime_base = MIMEBase('application', 'octet-stream')
            mime_base.set_payload(attach_file.read())
            encoders.encode_base64(mime_base)
            mime_base.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment)}')
            message.attach(mime_base)
            attach_file.close()
        
        # Set up the server and login
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send the email
        text = message.as_string()
        server.sendmail(EMAIL_ADDRESS, recipient, text)
        
        # Close the server connection
        server.quit()

        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {str(e)}")

# 3: Sending emails to a list of recipients with a template
def send_bulk_emails():
    recipients = [
        {'email': 'recipient1@example.com', 'name': 'Alice'},
        {'email': 'recipient2@example.com', 'name': 'Bob'}
    ]
    
    for recipient in recipients:
        # Using a template for the email body
        subject = f"Hello, {recipient['name']}!"
        body = f"Hi {recipient['name']},\n\nThis is an automated email just to keep in touch."
        attachment_path = '/path/to/report.pdf'  # Example attachment
        
        # Send the email
        send_email(recipient['email'], subject, body, attachment=attachment_path)

# 4: Schedule the email to be sent daily at a specific time (e.g., 9 AM)
def schedule_daily_email():
    schedule.every().day.at("09:00").do(send_bulk_emails)
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for a minute between schedule checks

if __name__ == "__main__":
    # Uncomment this line to test sending a single email
    # send_email('test@example.com', 'Test Subject', 'This is a test email.', attachment='/path/to/file.pdf')

    # Schedule the bulk email sending
    schedule_daily_email()