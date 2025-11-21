import json
import zlib

from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import time
def decode_body(req):
    """Decodes response body safely"""
    body = req.response.body
    encoding = req.response.headers.get('Content-Encoding', '')
    try:
        if 'gzip' in encoding:
            # اگر gzip هست، ابتدا decompress کن
            body = zlib.decompress(body, zlib.MAX_WBITS|16)
        return body.decode('utf-8')
    except Exception as e:
        return f"[Could not decode body: {e}]"
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

    target = "SearchPopularPrices"

    print("=====NETWORK REQUESTS=====")
    for req in driver.requests:
        if req.response:
            try:
                print("Request Body:", req.body)
                print("Response Body:", req.response.body.decode('utf-8'))
            except:
                pass
    driver.quit()

if __name__ == "__main__":
    run_test()
