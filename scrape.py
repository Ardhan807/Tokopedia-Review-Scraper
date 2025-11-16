from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

url = 'https://www.tokopedia.com/fantech-official-store/review'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

data = []

def click_all_read_more(driver):
    while True:
        try:
            # cari semua tombol "Baca Selengkapnya"
            buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Selengkapnya')]")
            
            if not buttons:
                break  # tidak ada tombol lagi
            
            for btn in buttons:
                try:
                    driver.execute_script("arguments[0].click();", btn)
                    time.sleep(0.3)
                except:
                    continue
        except:
            break

for page in range(0, 3):   # jumlah halaman yang ingin discan
    print("Scraping page:", page+1)
    click_all_read_more(driver)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    containers = soup.find_all("article", {"class": "css-1pr2lii"})

    for c in containers:
        # REVIEW
        review = c.find("span", {"data-testid": "lblItemUlasan"})
        review = review.text.strip() if review else None

        # RATING
        rating_tag = c.find("div", {"data-testid": "icnStarRating"})
        if rating_tag:
            aria = rating_tag.get("aria-label")  # contoh: "bintang 5"
            try:
                rating = int(aria.split()[-1])
            except:
                rating = None
        else:
            rating = None

        # PRODUK
        produk = c.find("p", {"class": "css-akhxpb-unf-heading"})
        produk = produk.text.strip() if produk else None

        try:
            likes = like.text.strip()
        except:
            likes = None

        data.append([
            review, rating, produk,
        ])

    # NEXT PAGE
    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']")
        next_btn.click()
        time.sleep(3)
    except:
        print("No more pages")
        break

driver.quit()

# Save CSV
df = pd.DataFrame(data, columns=[
    "review", "rating", "produk",
])

df.to_csv("fantech_review.csv", index=False)
print("Saved: fantech_review.csv")
