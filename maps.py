import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_logged_driver():
    GMAIL = 'bbeloshitskyy@gmail.com'
    # GMAIL = 'stepanbandera202202@gmail.com'
    # PASSWORD = 'BanderaUARU1221'
    PASSWORD = 'Berlintowel107!'
    for _ in range(20):
        driver = None
        try:
            chrome_options = uc.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--profile-directory=Default")
            chrome_options.add_argument("--user-data-dir==./tmp")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("user_agent=DN")
            # driver = uc.Chrome(options=chrome_options)
            driver = webdriver.Chrome(options=chrome_options)

            # driver = uc.Chrome(options=chrome_options)
            driver.delete_all_cookies()
            driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(GMAIL)
            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)
            time.sleep(10)
            driver.find_element(By.XPATH, "//input[@type='password']").send_keys(PASSWORD)
            driver.find_element(By.XPATH, "//input[@type='password']").send_keys(Keys.RETURN)
            time.sleep(10)
            return driver
        except:
            driver.close()
            time.sleep(5)
            print("Attempt failed, retry")


def go_to_place(driver, search_query):
    # search_query = "ул. Пятницкая, 5, Москва, Росія, 115035  Coffee Bean"
    url = f"https://www.google.com/search?q={search_query}"
    driver.get(url)


def post_a_message(driver):
    driver.find_element(By.CSS_SELECTOR, "span.wrsf").click()
    time.sleep(2)
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe.goog-reviews-write-widget"))
    driver.find_element(By.CSS_SELECTOR, "textarea").send_keys(" Слава Україні, не перезвонят ")
    # driver.find_element(By.CSS_SELECTOR, "textarea").send_keys("Заберите своих Ванек из Пемзы, росияни умирают приходя в Украину. Не отправляйте сыновей на убой.Славa Украине")
    driver.find_element(By.CSS_SELECTOR, 'div[data-rating="3"]').click()
    driver.find_element(By.XPATH, "//button[.//span[text()='Post']]").click()


if __name__ == '__main__':
    driver = get_logged_driver()
    go_to_place(driver, "ул. Пятницкая, 8, Москва, Росія, Cofix")
    post_a_message(driver)