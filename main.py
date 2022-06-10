
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

s=Service(r"C:\Users\Pranav goel\Desktop\seleniumDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.booking.com/")


def select_currency(currency):
    currency_button = driver.find_element(By.CSS_SELECTOR, 'button[data-modal-aria-label="Select your currency"]')
    currency_button.click()
    selected_currency = driver.find_element(By.CSS_SELECTOR,
                                            'a[data-modal-header-async-url-param*='
                                            f'"changed_currency=1&selected_currency={currency}&top_currency=1"]')
    selected_currency.click()


def search_customization(place, starting_date, ending_date, adults, rooms):
    # place customization
    search_element = driver.find_element(By.ID, 'ss')
    search_element.click()
    search_element.clear()
    search_element.send_keys(place)

    # date customization
    start_date_button = driver.find_element(By.CSS_SELECTOR, 'div[class="xp__dates-inner"]')
    start_date_button.click()
    start_date = driver.find_element(By.CSS_SELECTOR, f'td[data-date="{starting_date}"]')
    start_date.click()
    end_date = driver.find_element(By.CSS_SELECTOR, f'td[data-date="{ending_date}"]')
    end_date.click()

    # guest customization
    guest_no = driver.find_element(By.CSS_SELECTOR, 'label[id="xp__guests__toggle"]')
    guest_no.click()

    adult_children_room = driver.find_element(By.CSS_SELECTOR, 'span[class="bui-stepper__display"]')
    adult = int(adult_children_room.text)
    # children = 0
    room = 1
    while adult != 1:
        adult = adult - 1
        adult_decrease = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
        adult_decrease.click()

    while adult != adults:  # 5 adults
        adult = adult + 1
        adult_increase = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
        adult_increase.click()
    # while children != 1:
    #     children = children+1
    #     children_increase = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Children"]')
    #     children_increase.click()
    # age_select = driver.find_element(By.CSS_SELECTOR, 'select[data-group-child-age="0"]')
    # age_select.click()
    # option_value = driver.find_element(By.CSS_SELECTOR, 'option[value="7"]')
    # option_value.click()
    # age_select.click()

    while room != rooms:  # 2 rooms
        room = room + 1
        room_increase = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]')
        room_increase.click()


def search_submit():
    search_submit_button = driver.find_element(By.CSS_SELECTOR, 'span[class="js-sb-submit-text "]')
    search_submit_button.click()


def filters(stars):
    star_filter = driver.find_element(By.CSS_SELECTOR, f'div[data-filters-item="class:class={stars}"]')
    star_filter.click()

    lowest_price_sort = driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]')
    lowest_price_sort.click()


def pull_hotel_names():
    list_of_hotels = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="title"]')
    for i in list_of_hotels:
        print(i.text)


driver.implicitly_wait(15)
select_currency("USD")
search_customization('New York', "2022-07-25", "2022-07-25", 5, 2)
search_submit()
filters("5")
time.sleep(4)
driver.refresh()
pull_hotel_names()
