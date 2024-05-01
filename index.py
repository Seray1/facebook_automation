from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
wait = WebDriverWait(driver, 10)
# login details
phonenumber = 'your phone number or email'
password = 'your password'
def scroll_and_click(driver,xpath,wait):
    element_to_click = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", element_to_click)
    driver.execute_script("arguments[0].click();", element_to_click)

def scroll_and_fill(driver,xpath, value,wait):
    element_to_fill = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", element_to_fill)
    driver.execute_script("arguments[0].value = arguments[1];",element_to_fill,value,)

def scroll_and_click_by_text(driver,text,wait):
    element_to_click = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", element_to_click)
    driver.execute_script("arguments[0].click();", element_to_click)

def automate_facebook():
    try:
        scroll_and_fill(driver,'//*[@id="email"]', phonenumber,wait)
        scroll_and_fill(driver,'//*[@id="pass"]', password,wait)
        time.sleep(2)
        login_btn = wait.until(EC.presence_of_element_located((By.NAME, 'login')))
        driver.execute_script("arguments[0].scrollIntoView(true);", login_btn)
        driver.execute_script("arguments[0].click();", login_btn)
        time.sleep(5)
        # go to timeline
        scroll_and_click_by_text(driver,'Charles Okon',wait)
        time.sleep(10)
        # get post
        # adjust the range to the number of post to be deleted e.g range(100) to delete 100 post
        for i in range(10):
            time.sleep(3)
            post = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Actions for this post"]')))
            time.sleep(2)
            post.click()
            move_to = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), 'Move to bin')]")))
            time.sleep(2)
            move_to.click()
            move = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Move"]')))
            time.sleep(2)
            move.click()
            print(f'deleted')
    except Exception as e:
        print(e)

automate_facebook()    

