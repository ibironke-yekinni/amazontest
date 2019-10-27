from selenium  import webdriver
from time import sleep

class WebDriver:
    def __init__(self):
        self.myDriver = webdriver.Chrome(r"C:\Users\ibironke.yekinni\PycharmProjects\Training\driver\chromedriver.exe")

    def fetchUrl(self):
        self.myDriver.get("https://www.amazon.co.uk/")
        self.myDriver.maximize_window()
    def shutdown(self):
        sleep(5)
        self.myDriver.quit()