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

    driver.get("https://www.flytoday.ir/")
    time.sleep(5)

    print("=====NETWORK REQUESTS=====")
    for req in driver.requests:
        if req.response:
            print("URL:", req.url)
            print("Method:", req.method)
            print("Status:", req.response.status_code)
            print("Request Headers:", req.headers)
            print("Response Headers:", req.response.headers)
            print("=" * 50)


    driver.quit()

if __name__ == "__main__":
    run_test()
