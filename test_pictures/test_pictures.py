import allure
import time
import re

from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# exec_path_chrome = 'drivers/chromedriver.exe'
# options = webdriver.ChromeOptions()
# options.binary_location =exec_path_chrome


# Тестирование 2.1 Перейти в “Вышитые картины”, произвести поиск по жанру
# «Городской пейзаж», проверить, что картина “Трамвайный путь”
# присутствует в выдаче. (Chrome)
@allure.story("The test of the existence of the Tram picture in the list, Chrome")
@allure.feature("Testing point 1 Chrome")
@allure.severity("blocker")
def test_chrome_tram_exists():
    with allure.step("Create a driver, open the window to full screen, go to the website"):
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Open the drop-down list"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Moving on to the embroidered paintings"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(8) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Screenshots error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Choosing the Urban Landscape genre"):
        try:
            city_landscape = driver.find_element(By.CSS_SELECTOR,
                                                 "#genrebox > div > label:nth-child(2)")
            city_landscape.click()
            city_landscape.send_keys(Keys.ENTER)
            time.sleep(3)
        except Exception as e:
            print(e)
            with allure.step("Screenshots error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Looking for a tramway among the paintings"):
        try:
            response = re.findall(r'<meta itemprop="description" content="(.*)">', str(driver.page_source))
            flag = False
            for item in response:
                if "Трамвайный путь" in item:
                    flag = True
        except Exception as e:
            print(e)
            with allure.step("Screenshots error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()

    try:
        assert flag
    except AssertionError("The specified painting is not in the list"):
        with allure.step("Screenshots error"):
            allure.attach(driver.get_screenshot_as_png(), name="chrome_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()

    with allure.step("Closing driver"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Screenshots error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()

# Тестирование 2.1 Перейти в “Вышитые картины”, произвести поиск по жанру
# «Городской пейзаж», проверить, что картина “Трамвайный путь”
# присутствует в выдаче. (Firefox)
@allure.story("The test of the existence of the Tram picture in the list, Firefox")
@allure.feature("Testing point 1 Firefox")
@allure.severity("critical")
def test_firefox_tram_exists():
    with allure.step("Create a driver, open the window to full screen, go to the website"):
        try:
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Open the drop-down list"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Moving on to the embroidered paintings"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(8) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Choosing the Urban Landscape genre"):
        try:
            city_landscape = driver.find_element(By.CSS_SELECTOR,
                                                 "#genrebox > div > label:nth-child(2)")
            city_landscape.click()
            time.sleep(3)
            use = driver.find_element(By.CSS_SELECTOR, "#applymsg")
            use.click()
            time.sleep(3)
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Looking for a tramway among the paintings"):
        try:
            response = re.findall(r'<meta itemprop="description" content="(.*)">', str(driver.page_source))
            flag = False
            for item in response:
                if "Трамвайный путь" in item:
                    flag = True
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()

    try:
        assert flag
    except AssertionError("There are no pict in lis"):
        with allure.step("Taking a screenshot of the error"):
            allure.attach(driver.get_screenshot_as_png(), name="firefox_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()

    with allure.step("Closing driver"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()


# 2.2 Перейти в “Вышитые картины”, произвести поиск по жанру
# «Городской пейзаж», открыть подробности картины “Трамвайный путь”,
# проверить, что стиль картины «Реализм». (Chrome)
@allure.story("A test of the genre of the Tramway painting - realism, Chrome")
@allure.severity("blocker")
def test_chrome_tram_genre():
    with allure.step("Create a driver, open the window to full screen, go to the website"):
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://artnow.ru")
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Open the drop-down list"):
        try:
            drop_down_list = driver.find_element(
                By.CSS_SELECTOR,
                "#left_container > div > ul:nth-child(2) > li.menu-group.gids > div")
            drop_down_list.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Moving on to the embroidered paintings"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(8) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Choosing the Urban Landscape genre"):
        try:
            city_landscape = driver.find_element(By.CSS_SELECTOR,
                                                 "#genrebox > div > label:nth-child(2)")
            city_landscape.click()
            city_landscape.send_keys(Keys.ENTER)
            time.sleep(3)
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Looking for a tramway among the paintings"):
        try:
            tram_track = driver.find_element(By.CSS_SELECTOR, "#sa_container > div:nth-child(5) > a > div")
            tram_track.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Check the genre of the painting for realism"):
        try:
            response = str(re.search(r'Стиль: (.*?)\.', str(driver.page_source)).group())
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert "реализм" in response
    except AssertionError("Current genre - not realism"):
        with allure.step("Taking a screenshot of the error"):
            allure.attach(driver.get_screenshot_as_png(), name="chrome_error", attachment_type=AttachmentType.PNG)
        driver.close()
        driver.quit()
    with allure.step("Closing driver"):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()