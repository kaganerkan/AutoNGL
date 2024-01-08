import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def AskwithNGL(Target,message,link_type): 
    options = Options()
    options.headless = True
    driver = uc.Chrome(options=options)

    def detect_label_and_submit(driver):
        text_box = driver.find_element(By.ID, "question")
        text_box.send_keys(str(message))
        submit_button = driver.find_element(By.CLASS_NAME, "submit")
        submit_button.click()

    if link_type == str("confess"):
        driver.get("https://confess.ngl.link/"+Target)
    elif link_type == str("3words"):
        driver.get("https://3words.ngl.link/"+Target)
    elif link_type == str("wfriendship"):
        driver.get("https://ngl.link/"+Target+"/wfriendship")
    elif link_type == str("rizzme"):
        driver.get("https://ngl.link/"+Target+"/rizzme")
    elif link_type == str("wfriendship"):
        driver.get("https://ngl.link/"+Target+"/WFRIENDSHIP")
    elif link_type == str("tbh"):
        driver.get("https://ngl.link/"+Target+"/tbh")
    elif link_type == str("shipme"):
        driver.get("https://ngl.link/"+Target+"/shipme")
    elif link_type == str("yourcrush"):
        driver.get("https://ngl.link/"+Target+"/yourcrush")
    elif link_type == str("cancelled"):
        driver.get("https://ngl.link/"+Target+"/cancelled")
    elif link_type == str("dealbreaker"):
        driver.get("https://ngl.link/"+Target+"/dealbreaker")
    else:
        driver.get("https://ngl.link/"+Target)

    driver.maximize_window()
    detect_label_and_submit(driver)
    driver.close()
