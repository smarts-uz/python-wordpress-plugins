from django.utils import timezone
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import os
import django

# Django sozlamalarini yuklash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'woocommerce.settings')
django.setup()

from products.models import Product

# Chrome options sozlamalari
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Xoxlasangiz, headless rejimni yoqing

# Chrome driverni ishga tushirish
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL manzili
url = "https://woocommerce.com/product-category/woocommerce-extensions/"
pagination='?categoryIds=1021&collections=product&page='
page_count=1

# Kutish sozlamalari
wait = WebDriverWait(driver, 10)


# Narxni faqat $99 shaklida olish uchun funksiya
def clean_price(price_text):
    # Faqat $ belgisi bilan boshlangan raqamlarni olish
    match = re.search(r'\$\d+', price_text)
    return match.group() if match else 'Price Not Listed'


# Sahifalarda yurish uchun loop
while True:
    try:
        print(f"\n--- Sahifa {page_count} boshlanmoqda... ---")
        # Update the URL for the current page
        base_url = url + pagination + str(page_count)
        driver.get(base_url)

        # Sahifadagi barcha kartalarni yuklash
        product_cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'wccom-comp-card-product')))

        for card in product_cards:
            try:
                # Mahsulot ma'lumotlarini olish
                product_name = card.find_element(By.CLASS_NAME, 'wccom-card__title').text.strip()
                product_link = card.find_element(By.CLASS_NAME, 'wccom-card__title-link').get_attribute('href')
                vendor_name = card.find_element(By.CLASS_NAME, 'wccom-card__vendor').text.strip().replace('by',
                                                                                                          '').strip()
                description = card.find_element(By.CLASS_NAME, 'wccom-card__content').text.strip()

                # Tavsif va reytingni ajratish
                rating = None
                if "Rated" in description:
                    rating = description.split("Rated")[1].split("out")[0].strip()

                reviews = re.search(r'\((\d+)\)', description)
                reviews = reviews.group(1) if reviews else None

                # Narxni olish
                try:
                    price_element = WebDriverWait(card, 2).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'wccom-product-card__price'))
                    )
                    raw_price = price_element.text.strip()

                    if 'Loading price' in raw_price:
                        time.sleep(2)
                        raw_price = price_element.text.strip()

                    if 'Free download' in raw_price:
                        price = 'Free'
                    else:
                        price = clean_price(raw_price)

                except Exception as e:
                    print(f"Price olishda xato: {e}")
                    price = 'Price Not Listed'
                if Product.objects.filter(link=product_link).exists():
                    print(f"🔸 {product_name} - bu mahsulot allaqachon mavjud. Davom etmoqda...")
                    continue  # Mahsulot mavjud bo'lsa, davom etish

                # Ma'lumotlarni terminalga chiqarish
                print(f"🔹 Product Name: {product_name}")
                print(f"🔹 Product Link: {product_link}")
                print(f"🔹 Vendor Name: {vendor_name}")
                print(f"🔹 Description: {description[:60]}...")
                print(f"🔹 Rating: {rating}")
                print(f"🔹 Reviews: {reviews}")
                print(f"🔹 Price: {price}")
                print("=" * 60)

                # Django ORM orqali ma'lumotlarni saqlash
                Product.objects.create(
                    name=product_name,
                    link=product_link,
                    vendor_name=vendor_name,
                    description=description,
                    rating=rating,
                    reviews=reviews,
                    price=price,
                    created_at=timezone.now()
                )

            except Exception as e:
                print(f"Karta o‘qishda xato: {e}")

        # Sahifada navbatdagi sahifani topish
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.page-numbers.next')))
            next_page = next_button.get_attribute('href')

            if next_page:
                print(f"Keyingi sahifa: {next_page}")
                page_count += 1
                time.sleep(3)
            else:
                print("✅ Barcha sahifalar tugadi.")
                break

        except Exception as e:
            print(f"Sahifa o‘tkazishda xato: {e}")
            break

    except Exception as e:
        print(f"Umumiy xato: {e}")
        break

# Brauzerni yopish
driver.quit()
