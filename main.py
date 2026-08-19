import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("URL")
email = os.getenv("ACCOUNT_EMAIL")
password = os.getenv("PASSWORD")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def login(origin):
    # driver.get(url)
    login_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-tindog-login")))
    login_btn.click()

    face_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-facebark")))
    face_btn.click()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != origin:
            driver.switch_to.window(window_handle)

            email_input = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
            email_input.send_keys(email)
            password_input = wait.until(EC.element_to_be_clickable((By.NAME, "pass")))
            password_input.send_keys(password)
            submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            submit_btn.click()

    driver.switch_to.window(origin)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Allow"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Not interested"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="I Accept"]'))).click()

    if wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "swipe-card-info"))):
        print("Login Successful")

try:
    driver.get(url)
    original_window = driver.current_window_handle

    login(original_window)
finally:
    time.sleep(60)
    driver.quit()