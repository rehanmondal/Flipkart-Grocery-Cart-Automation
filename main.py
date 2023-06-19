#  ======= Author : REHAN MONDAL ========
#  ======= Date   : June,18,2023 ========
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
import os
import time

driver = webdriver.Chrome()
url = "https://www.flipkart.com/search?q=sugar%201%20kg&otracker=search&otracker1=search&marketplace=GROCERY&as-show=on&as=off"

# ~~~  reading items list ~~~
item_list = []
print("\n============================ FLIPKART   GROCERY   AUTOMATION ===============================")
print("============================ Automation Started Successfully ===============================\n")
try:
    f = open("D:\\SELENIUM\FLIPKART_GROCCERY\\items.txt","r")   # Set location accordingly where user's item list is present
    item_list = f.readlines()
    no_of_items = len(item_list)
    print("Items read successfully from text file")
except:
    print("!!! Issue in reading items list")

# ~~~  Get the url ~~~
try:
    driver.maximize_window()
    driver.get(url)
    print("Home page loaded Succesfully")
except:
    print("!!! Unable to load Home Page")

# ~~~  Entering Pincode ~~~
try:
    time.sleep(8)
    driver.find_element(By.XPATH, "//input[contains(@name, 'pincode')]").send_keys('700154',Keys.RETURN)
    time.sleep(8)
    print("Pincode put Succesfully")
except:
    print("!!! Unable to put pincode")

# ~~~  Check Visibility for search box ~~~
try:
    driver.find_element(By.XPATH, "//input[contains(@name, 'q')]").clear()
    print("Search box found and clear succesfully")
except:
    print("!!! Unable to find search box")

# ~~~  find product in search box ~~~
try:
    print(f"Total number of products available in the list is {no_of_items}")
    try:
        for product in range(no_of_items):
            one_product = item_list[product][:-2]
            driver.find_element(By.XPATH,"//input[contains(@name, 'q')]").send_keys(one_product,Keys.RETURN)
            print(f"\n{product+1} no. product searched Succesfully")
            time.sleep(4)
            # ~~~ list item qty. and website item qty. matching ~~~
            try:
                list_quantity = [int(s) for s in one_product.split() if s.isdigit()]
                list_quan = list_quantity[0]
                web_q1 = driver.find_element(By.XPATH,"//div[contains(@class, '_1MbXnE _1kHdUD')]").text
                web_q2 = [int(t) for t in web_q1.split() if t.isdigit()]
                web_q3 = web_q2[0]
                print("Customer requrements : ",list_quan)
                print("Website Availabe     : ",web_q3)

                # ~~~ If qty. avl. then add to cart ~~~
                if list_quan == web_q3:
                    driver.find_element(By.XPATH,"//button[contains(@class, '_2KpZ6l GX4Kov')]").click()
                    time.sleep(2)
                    print(f"{product+1} no. product added to Cart Succesfully\n")
                else:
                    print("Quantity Not Available")
            except:
                print("!!! Unable to click on Add To Cart")

            # ~~~ clearing previous search item ~~~
            elem = driver.find_element(By.XPATH, "//input[contains(@class, '_3704LK')]")
            elem.send_keys(Keys.CONTROL,"a")
            elem.send_keys(Keys.BACK_SPACE)
            time.sleep(4)

    except  Exception as e:
        print("!!! Unable to fetch and put item one by one in the box")
        print(e)
except Exception as e:

    print(e)
    print("!!! Unable to put product in the search box")

# ~~~ View Cart ~~~
try:
    driver.find_element(By.XPATH, "//a[contains(@class, '_3SkBxJ')]").click()
    print("View Cart Clicked Successfully")
except:
    print("!!! Unable to view My Cart")

# ~~~ Fetching Cart Amount ~~~
try:
    time.sleep(8)
    amount = driver.find_element(By.XPATH, "(//div[contains(@class, 'z4Ha90')])[1]").text   
    #(//div[contains(@class, 'z4Ha90')])[2]//span
    time.sleep(2)
    print(f"Total Amount for the cart elements are : {amount}")
except Exception as e:
    print(e)
    print("!!! Unable to show Total Cart due Amount")

time.sleep(8)
print("\n============================ Automation Completed Successfully ===============================\n")