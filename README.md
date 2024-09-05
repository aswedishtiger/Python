# Python Automation Projects

This repository contains Python automation scripts for various use cases, including file automation, email automation, web scraping, and browser task automation using Selenium. These projects can be easily extended and integrated into larger automation systems, making them great additions to any portfolio.

## Table of Contents
1. [File Organization Automation](#file-organization-automation)
2. [Web Scraping with Python](#web-scraping-with-python)
3. [Email Automation](#email-automation)
4. [Task Automation with Selenium](#task-automation-with-selenium)
5. [Installation and Setup](#installation-and-setup)
6. [Usage](#usage)

---

## File Organization Automation

This script automatically organizes files in a specified directory by their file extension, creating folders for each extension and moving the files accordingly.

### Features
- Organizes files based on their extension.
- Automatically creates folders for different file types.
  
### Example Usage
```bash
python organize_files.py
```

### Sample Code
```python
import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(directory, ext.upper())
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(ext_folder, filename))

directory_path = "/path/to/your/directory"
organize_files(directory_path)
```

---

## Web Scraping with Python

This script demonstrates how to scrape data from a website and store it in a CSV file. The code uses `BeautifulSoup` and `requests` for web scraping.

### Features
- Scrapes data from a webpage.
- Saves the scraped data into a CSV file.

### Example Usage
```bash
python scrape_data.py
```

### Sample Code
```python
import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find_all('some_html_element')  # Modify as per the website structure
    return data

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Header1', 'Header2'])  # Modify headers based on the data
        for row in data:
            writer.writerow(row)

url = 'https://example.com'
scraped_data = scrape_data(url)
save_to_csv(scraped_data, 'output.csv')
```

---

## Email Automation

This script automates sending emails, either one-off or in bulk, with the option to attach files. The credentials are stored securely using environment variables.

### Features
- Send bulk emails using a list of recipients.
- Personalized email content with an email template.
- Optionally attach files like reports, PDFs, etc.
- Schedule emails to be sent at a specific time (e.g., daily).

### Example Usage
```bash
python email_automation.py
```

### Sample Code
```python
import smtplib
import os
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

EMAIL_ADDRESS = os.getenv('EMAIL_USER', 'your_email@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS', 'your_email_password')

def send_email(recipient, subject, body, attachment=None):
    try:
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = recipient
        message['Subject'] = subject
        
        message.attach(MIMEText(body, 'plain'))
        
        if attachment:
            attach_file = open(attachment, 'rb')
            mime_base = MIMEBase('application', 'octet-stream')
            mime_base.set_payload(attach_file.read())
            encoders.encode_base64(mime_base)
            mime_base.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment)}')
            message.attach(mime_base)
            attach_file.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = message.as_string()
        server.sendmail(EMAIL_ADDRESS, recipient, text)
        server.quit()

        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {str(e)}")

def send_bulk_emails():
    recipients = [
        {'email': 'recipient1@example.com', 'name': 'Alice'},
        {'email': 'recipient2@example.com', 'name': Bob}
    ]
    
    for recipient in recipients:
        subject = f"Hello, {recipient['name']}!"
        body = f"Hi {recipient['name']},\n\nThis is an automated email just to keep in touch."
        attachment_path = '/path/to/report.pdf'  # Example attachment
        send_email(recipient['email'], subject, body, attachment=attachment_path)

def schedule_daily_email():
    schedule.every().day.at("09:00").do(send_bulk_emails)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    schedule_daily_email()
```

---

## Task Automation with Selenium

This script automates common browser tasks using Selenium, such as logging into a website, filling out forms, and scraping data. It can also be expanded to automate file downloads or other tasks.

### Features
- Automate browser interactions (login, form submission, etc.).
- Scrape data from websites after interaction.
- Download files via automated clicks.

### Example Usage
```bash
python selenium_automation.py
```

### Sample Code
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

def login_to_website():
    driver.get('https://example.com/login')
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    username.send_keys('your_username')
    password.send_keys('your_password')
    password.send_keys(Keys.RETURN)
    time.sleep(2)

def navigate_to_form():
    driver.get('https://example.com/form-page')
    time.sleep(2)

def fill_out_form():
    first_name = driver.find_element(By.NAME, 'first_name')
    last_name = driver.find_element(By.NAME, 'last_name')
    email = driver.find_element(By.NAME, 'email')
    first_name.send_keys('John')
    last_name.send_keys('Doe')
    email.send_keys('john.doe@example.com')
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()
    time.sleep(2)

def scrape_data():
    success_message = driver.find_element(By.CLASS_NAME, 'success-message').text
    print(f"Success Message: {success_message}")

if __name__ == '__main__':
    try:
        login_to_website()
        navigate_to_form()
        fill_out_form()
        scrape_data()
    finally:
        driver.quit()
```

---

## Installation and Setup

### Requirements
- Python 3.x
- Required Python modules:
  - `requests`
  - `beautifulsoup4`
  - `smtplib` (standard library)
  - `schedule`
  - `selenium`
  
### Installing Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-automation-projects.git
   ```

2. Navigate to the project directory:
   ```bash
   cd python-automation-projects
   ```

3. Run individual scripts based on your automation needs:
   ```bash
   python organize_files.py
   python email_automation.py
   python selenium_automation.py
   ```

4. For Selenium, ensure you have downloaded the correct WebDriver for your browser and specify the correct path in the script.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize and extend these automation scripts to suit your needs!
