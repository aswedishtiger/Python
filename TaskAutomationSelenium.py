from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (Make sure you have the correct path to your WebDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# 1: Navigate to Login Page
def login_to_website():
    driver.get('https://example.com/login')  # Replace with the actual login page URL

    # Locate the username and password fields
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')

    # Input your login credentials
    username.send_keys('your_username')
    password.send_keys('your_password')

    # Submit the form by pressing Enter or clicking the submit button
    password.send_keys(Keys.RETURN)

    # Wait for page load
    time.sleep(2)  # Adjust time as needed

# 2: Navigate to Form Page after login
def navigate_to_form():
    # Assuming the form is on a separate page after login, navigate to that page
    driver.get('https://example.com/form-page')  # Replace with the actual form page URL
    time.sleep(2)

# 3: Fill out the form and submit
def fill_out_form():
    # Locate form fields by their name, id, or class
    first_name = driver.find_element(By.NAME, 'first_name')
    last_name = driver.find_element(By.NAME, 'last_name')
    email = driver.find_element(By.NAME, 'email')

    # Fill out the form fields
    first_name.send_keys('John')
    last_name.send_keys('Doe')
    email.send_keys('john.doe@example.com')

    # Optionally interact with dropdowns or radio buttons
    country_dropdown = driver.find_element(By.ID, 'country')
    country_dropdown.send_keys('United States')

    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()

    time.sleep(2)

# 4 (Optional): Scrape Data from the next page after form submission
def scrape_data():
    # Example: scraping a message or a table after form submission
    success_message = driver.find_element(By.CLASS_NAME, 'success-message').text
    print(f"Success Message: {success_message}")

    # If there's a table to scrape:
    table = driver.find_element(By.ID, 'data-table')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, 'td')
        row_data = [col.text for col in columns]
        print(row_data)

# 5 (Optional): Download a file after submission
def download_file():
    # Locate the download link
    download_link = driver.find_element(By.LINK_TEXT, 'Download Report')
    download_link.click()
    time.sleep(5)  # Wait for the file to download (you may want to handle this better)

# Main execution flow
if __name__ == '__main__':
    try:
        login_to_website()
        navigate_to_form()
        fill_out_form()
        scrape_data()  # Optionally scrape data after submission
        # download_file()  # Optionally download a file
    finally:
        # Close the browser when done
        driver.quit()