import random
import time

from selenium import webdriver

from selenium.webdriver import Keys
from PageObject.locators import *

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://qa-scooter.praktikum-services.ru/order")

driver.find_element(*MainPageLocators.BUTTON_ACCEPT_COOKIES).click()

driver.find_element(*OrderPageLocators.FIELD_NAME).send_keys("Денис")
driver.find_element(*OrderPageLocators.FIELD_LAST_NAME).send_keys("Денисов")
driver.find_element(*OrderPageLocators.FIELD_ADDRESS_WHERE_TO_TAKE).send_keys("Москва")
driver.find_element(*OrderPageLocators.FIELD_PHONE_NUMBER).send_keys("89771234567")
bootstrap = driver.find_element(*OrderPageLocators.BOOTSTRAP)
bootstrap.send_keys("Сокольники")
bootstrap.send_keys(Keys.ARROW_DOWN + Keys.ENTER)

driver.find_element(*OrderPageLocators.NEXT).click()

driver.find_element(*AboutRentLocators.WHEN_TO_BRING).send_keys("09.05.2023")

index = random.randint(0, 6)
color = random.randint(0, 1)
driver.find_element(*AboutRentLocators.DROPDOWN_ARROW).click()
driver.find_elements(*AboutRentLocators.DROPDOWN_MENU)[6].click()

driver.find_elements(*AboutRentLocators.SCOOTER_COLORS)[color].click()

driver.find_element(*AboutRentLocators.COMMENT_FOR_THE_COURIER).send_keys("Привозите после 12:00")

driver.find_element(*AboutRentLocators.BUTTON_TO_ORDER).click()
driver.find_elements(*AboutRentLocators.MODAL_FORM_BUTTONS)[1].click()

time.sleep(3)
print(driver.find_element(*OrderPageLocators.ORDER_STATUS_INFO).text)

print("Заказ оформлен" in driver.find_element(*OrderPageLocators.ORDER_STATUS_INFO).text)

time.sleep(1)
driver.quit()
