from selenium import webdriver
from time import sleep
import sys

CHROMEDRIVER_PATH = "C:\python3\Scripts\chromedriver.exe"

BELL_HOMEPAGE = "https://www.bell.ca/Mobility/Smartphones_and_mobile_internet_devices"

VALID_DRIVER_MSG = "Please select a valid webdriver to run this application. Default is: chrome"
INPUT_MSG = "Please select the device number for pricing details: "

DEVICE_ITEM_XPATH = "//*[@id='div_product_list_item_div_product_list_item_{}']/div/div[3]"
LINK_TO_DEVICE = "/html/body/main/div[5]/div/div[3]/div[{}]/div/a"
PLAN_DETAILS = "//*[@id='bcx-order-now-group-smartpay']/div[1]"
DEVICE_DETAILS = "//*[@id='productPriceDiv']/div[1]/div/div/div[2]/div[1]/h1"


####### Initialize webdriver #######
def init_driver(browser="chrome"):
    if (browser != "chrome"):
        raise Exception(VALID_DRIVER_MSG)
    else:
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
        return driver


####### Welcome Message #######
def welcome_user(name="Jatin"):
    print("Welcome, {} !! Please find the list of top 12 devices below:".format(name))



def get_page(driver, page):
    driver.get(page)

def maximize_window(driver):
    driver.maximize_window()


def wait_implicitly(driver, time=1000):
    driver.implicitly_wait(time)

def print_chars(char="-", times=1):
    print(char * times)

def shutdown_application(driver):
    driver.quit()
    sys.exit(0)

if __name__ == "__main__":
    try:
        driver = init_driver(browser="chrome")
        welcome_user(name="Harman")
        get_page(driver, BELL_HOMEPAGE)
        wait_implicitly(driver, time=100)
        sleep(20)
    except Exception as e:
        raise e
    finally:
        shutdown_application(driver)