import os
import json

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def ip_check_requests():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        ip = response.json().get('ip')
        print(f"[Requests] Your IP address is: {ip}")
    else:
        print("[Requests] Failed to get IP address.")

def ip_check_selenium():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Remote(
        command_executor=os.environ['SELENIUM_URL'],
        options=options,
    )
    try:
        driver.get('https://api.ipify.org?format=json')
        body_text = driver.find_element("tag name", "body").text
        ip = json.loads(body_text).get('ip')
        print(f"[Selenium] Your IP address is: {ip}")
    except Exception as e:
        print(f"[Selenium] Failed to get IP address: {e}")
    finally:
         driver.quit()


if __name__ == "__main__":
    ip_check_selenium()
    ip_check_requests()
