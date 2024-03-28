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


# 2.2 Перейти в “Вышитые картины”, произвести поиск по жанру
# «Городской пейзаж», открыть подробности картины “Трамвайный путь”,
# проверить, что стиль картины «Реализм». (Firefox)
@allure.story("Create a driver, open the window to full screen, go to the website")
@allure.severity("critical")
def test_firefox_tram_genre():
    with allure.step("Создаем драйвер, открываем окно на полный экран, переходим на сайт"):
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
            tram_track = driver.find_element(By.CSS_SELECTOR, "#sa_container > div:nth-child(5) > a > div")
            tram_track.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Check the genre of the painting for realism"):
        try:
            response = str(re.search(r'Стиль: (.*?)\.', str(driver.page_source)).group())
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert "реализм" in response
    except AssertionError("Current genre - not realism"):
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


# 2.3 Перейти в “Батик”, добавить первую картину в избранное, проверить,
# что выбранная картина сохранилась в разделе «Избранное». (Chrome)
@allure.story("The test of adding an item to favorites, Chrome")
@allure.severity("blocker")
def test_chrome_favorite():
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
    with allure.step("Go to batik"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(3) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Select the first picture and open it"):
        try:
            chosen_painting = driver.find_element(By.CSS_SELECTOR,
                                                  "#sa_container > div:nth-child(3) > a:nth-child(1) > div")
            chosen_painting.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), nname="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Add it to favorites, keeping the name"):
        try:
            response1 = str(re.findall('<title>«(.*?)» ', str(driver.page_source))[0])
            heart = driver.find_element(By.CSS_SELECTOR,
                                        "#main_container > div:nth-child(3) > div.infocontainer > div.sale-span > span")
            heart.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Go to favorites"):
        try:
            favorites = driver.find_element(By.CSS_SELECTOR, "body > div.topheader > span.fvtico > img")
            favorites.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Looking for the name of the painting in favorites"):
        try:
            fav_painting = driver.find_element(By.CSS_SELECTOR, "#sa_container > div.post > a:nth-child(1) > div")
            fav_painting.click()
            response2 = str(re.findall(r'<title>«(.*?)» ', str(driver.page_source))[0])
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert response1 == response2
    except AssertionError("If there is another picture in the favorites"):
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

# 2.3 Перейти в “Батик”, добавить первую картину в избранное, проверить,
# что выбранная картина сохранилась в разделе «Избранное». (Firefox)
@allure.story("he test of adding an item to favorites, Firefox")
@allure.severity("critical")
def test_firefox_favorite():
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
    with allure.step("Go to batik"):
        try:
            paintings = driver.find_element(By.CSS_SELECTOR,
                                            "#left_container > div > ul:nth-child(2) > li:nth-child(3) > a")
            paintings.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Select the first picture and open it"):
        try:
            chosen_painting = driver.find_element(By.CSS_SELECTOR,
                                                  "#sa_container > div:nth-child(3) > a:nth-child(1) > div")
            chosen_painting.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Add it to favorites, keeping the name"):
        try:
            response1 = str(re.findall('<title>«(.*?)» ', str(driver.page_source))[0])
            heart = driver.find_element(By.CSS_SELECTOR,
                                        "#main_container > div:nth-child(3) > div.infocontainer > div.sale-span > span")
            heart.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(),name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Go to favorites"):
        try:
            favorites = driver.find_element(By.CSS_SELECTOR, "body > div.topheader > span.fvtico > img")
            favorites.click()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Looking for the name of the painting in favorites"):
        try:
            fav_painting = driver.find_element(By.CSS_SELECTOR, "#sa_container > div.post > a:nth-child(1) > div")
            fav_painting.click()
            response2 = str(re.findall(r'<title>«(.*?)» ', str(driver.page_source))[0])
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="firefox_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert response1 == response2
    except AssertionError("If there is another picture in the favorites"):
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

# 2.4 Ввести в поисковую строку «Жираф», проверить, что название первой
# картины содержит слово «Жираф». (Chrome)
@allure.story("The test of searching the Жирафик, Chrome")
@allure.severity("blocker")
def test_chrome_giraffe():
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
    with allure.step("Opening the search line and searching for giraffe"):
        try:
            find_bar = driver.find_element(By.CSS_SELECTOR,
                                           "#MainSearchForm > div > div:nth-child(1) > input.inp.scLarge")
            find_bar.click()
            find_bar.send_keys('Жираф')
            find_bar.send_keys(Keys.ENTER)
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    with allure.step("Looking for giraffe in the result"):
        try:
            response = re.search(r'<meta itemprop="description" content="(.*?)">',
                                 str(driver.page_source)).group()
        except Exception as e:
            print(e)
            with allure.step("Taking a screenshot of the error"):
                allure.attach(driver.get_screenshot_as_png(), name="chrome_error",
                              attachment_type=AttachmentType.PNG)
            driver.close()
            driver.quit()
    try:
        assert "Жираф" in response
    except AssertionError("If there is no giraffe"):
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