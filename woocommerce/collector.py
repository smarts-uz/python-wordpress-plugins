import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import os
import django

# Set up Django settings for the scraper
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'woocommerce.settings')  # Sozlamalaringizni to'g'ri o'rnating
django.setup()
from products.models import Product  # Django modelini import qilish
# Set up Chrome options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Uncomment this line if you want to run in headless mode

# Set up ChromeDriver service
service = Service(ChromeDriverManager().install())

# Initialize the Chrome driver with the correct service and options
driver = webdriver.Chrome(service=service, options=options)

# URL of the first page to scrape
url = "https://woocommerce.com/product-category/woocommerce-extensions/"

driver.get(url)

# Explicit wait setup
wait = WebDriverWait(driver, 10)

# Loop through pages (assuming next page link exists)
while True:
    try:
        # Find all the product cards on the current page
        product_cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'wccom-comp-card-product')))

        for card in product_cards:
            # Extract product name
            product_name = card.find_element(By.CLASS_NAME, 'wccom-card__title').text.strip()

            # Extract product link
            product_link = card.find_element(By.CLASS_NAME, 'wccom-card__title-link').get_attribute('href')

            # Extract vendor name and remove "by"
            vendor_name = card.find_element(By.CLASS_NAME, 'wccom-card__vendor').text.strip().replace('by', '').strip()

            # Extract product description
            description = card.find_element(By.CLASS_NAME, 'wccom-card__content').text.strip()

            # Ratingni descriptiondan olish (agar mavjud bo'lsa)
            if "Rated" in description:
                rating = description.split("Rated")[1].split("out")[0].strip()
            else:
                rating = None  # Agar descriptionda rating bo'lmasa, None

            # Extract price, and handle "Free download" case
            try:
                price_text = card.find_element(By.CLASS_NAME, 'wccom-product-card__price').text.strip()
                if 'Free download' in price_text:
                    price = 'Free'
                else:
                    price = price_text
            except:
                price = 'Price Not Listed'  # If no price element found, set a default message

            # Extract review count
            reviews = re.search(r'\((\d+)\)', description)
            reviews = reviews.group(1) if reviews else None

            # Print the extracted information
            print(f"Product Name: {product_name}")
            print(f"Product Link: {product_link}")
            print(f"Vendor Name: {vendor_name}")
            print(f"Description: {description}")
            print(f"Rating: {rating}")
            print(f"Reviews: {reviews}")
            print(f"Price: {price}")
            print("-" * 50)

            # Save the product data into the SQLite database using Django ORM
            Product.objects.create(
                name=product_name,
                link=product_link,
                vendor_name=vendor_name,
                description=description,
                rating=rating,
                reviews=reviews,
                price=price
            )

        # Check for the "Next Page" button and navigate to the next page
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Next »')))
            next_button.click()
            time.sleep(3)  # Wait for the next page to load
        except:
            print("No more pages to scrape.")
            break  # Exit the loop if there's no next page

    except Exception as e:
        print(f"An error occurred: {e}")
        break  # Exit the loop on error

# Close the WebDriver
driver.quit()
