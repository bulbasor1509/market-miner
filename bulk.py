from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import service as s
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


class BulkScrapper:
    def __init__(self):
        self.df = None
        options = Options()
        # options.add_argument("--headless")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--window-size=1920,1080")  # Forces proper rendering
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=options)

    def crawl(self, url: str):
        self.driver.get(url)


    def run_scrapper(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dayslisting")))
        one_day_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul.dayslisting li a[data-val="1D"]')))
        self.driver.execute_script("arguments[0].click();", one_day_btn)
        time.sleep(1)
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#HistBulkBlockDataTable tbody tr")
        cols = self.driver.find_elements(By.CSS_SELECTOR, "#HistBulkBlockDataTable thead th")
        cols_heading = [col.text for col in cols]
        data = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            row_data = [col.text.strip() for col in cols]
            if row_data:
                data.append(dict(zip(cols_heading, row_data)))
        return data

    def quit_driver(self):
        self.driver.quit()