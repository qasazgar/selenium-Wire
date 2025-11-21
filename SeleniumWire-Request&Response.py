from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import time

def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(seleniumwire_options={
        'verify_ssl': False
    }, options=chrome_options)

    driver.get("https://www.scrapingcourse.com/api/products")
    time.sleep(5)

    print("=====NETWORK REQUESTS=====")
    for req in driver.requests:
        if req.response:
            print(req.method, req.url, req.response.status_code)

    driver.quit()

if __name__ == "__main__":
    run_test()
