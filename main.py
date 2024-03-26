import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def openSapling():
    print("Starting SaplingBot")
    browser = input("google or firefox (1 or 2)")
    driver = None
    if browser == "1":
        driver = webdriver.Chrome()
    if browser == "2":
        driver = webdriver.Firefox()

    if browser is None:
        quit("pick a number properly")

    driver.get("https://clever.com/in/bsd405/student/portal")
    time.sleep(random.random())

    x_path = "/html/body/div[3]/div/div/div[2]/div[1]/a[1]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path)))
    driver.find_element(By.XPATH, x_path).click()

    # with open("user.txt") as f:
    #     data = f.read()
    data = input("enter your bsd email: ")

    x_path = "//*[@id=\"i0116\"]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path)))
    sendKeys(driver.find_element(By.XPATH, x_path), data)

    x_path = "//*[@id=\"idSIButton9\"]"
    WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.XPATH, x_path)))
    driver.find_element(By.XPATH, x_path).click()

    time.sleep(1)
    # with open("pass.txt") as f:
    #     data = f.read()
    data = input("enter your bsd password: ")

    x_path = "//*[@id=\"i0118\"]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path)))
    sendKeys(driver.find_element(By.XPATH, x_path), data)

    x_path = "//*[@id=\"idSIButton9\"]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path)))
    driver.find_element(By.XPATH, x_path).click()

    time.sleep(2)
    x_path = "//*[@id=\"idSIButton9\"]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path)))
    driver.find_element(By.XPATH, x_path).click()

    time.sleep(2)
    print(driver.current_url)
    list = driver.find_element(By.CSS_SELECTOR, "div.Category--container:nth-child(5) > div:nth-child(3)")
    for element in list.find_elements(By.CSS_SELECTOR, "*"):
        if element.get_attribute(
                "class") == "self--start flexbox flex--direction--column items--center ResourceLink ResourceLink--size--small":
            if element.find_element(By.TAG_NAME, "img").get_attribute("title") == "Sapling Learning":
                element.click()

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "go-button")))
    driver.find_element(By.CLASS_NAME, "go-button").click()

    time.sleep(5)
    element = driver.find_element(By.CLASS_NAME, "divTable")
    getAssignment(element).find_element(By.CLASS_NAME, "divCellFirst").click()

    driver.switch_to.frame(driver.find_element(By.ID, "flcn_assignment"))
    while True:
        answerQuestion(driver)
        time.sleep(0.5)

    # driver.quit()


def getAssignment(element):
    for e in element.find_elements(By.CSS_SELECTOR, "*"):
        # print(e.get_attribute("class"))
        if e.get_attribute("class") == "divRow grey" or e.get_attribute("class") == "divRow white":
            for e1 in e.find_elements(By.CSS_SELECTOR, "*"):
                if e1.get_attribute("class") == "status error" or e1.get_attribute("class") == "status warning":
                    return e
    exit("No assignment to be completed")


def answerQuestion(driver):
    time.sleep(1)
    options = driver.find_elements(By.CLASS_NAME, "multichoice-column1")
    for x in range(len(options)):
        time.sleep(1)
        answer_button = driver.find_element(By.CLASS_NAME, "action-button")
        if answer_button.get_attribute("aria-label") == "Next Question":
            answer_button.click()
            return
        if answer_button.get_attribute("aria-label") == "Try Again":
            answer_button.click()
        if answer_button.get_attribute("aria-label") == "Resume":
            answer_button.click()
        try:
            options[x].click()
        except:
            print("could not2 click")
        time.sleep(0.5)
        if len(driver.find_elements(By.CLASS_NAME, "modal-solution-container")) > 0:
            driver.find_element(By.ID, "solution-modal-next-item").click()
            print("answer correct")
            time.sleep(1)
            return
        answer_button.click()
        answer_button.click()

    # for bubble in bubbles:
    #     e.click()
    #     driver.find_element(By.XPATH, "//*[@id=\"button-check\"]").click()

    # questions.find_elements(By.CLASS_NAME, "multichoice-column1")[0].click()
    # driver.find_element(By.XPATH, "//*[@id=\"button-check\"]").click()


def sendKeys(element, str):
    for char in str:
        element.send_keys(char)
        time.sleep(max(0.21, random.random() - 0.5))


if __name__ == '__main__':
    openSapling()
