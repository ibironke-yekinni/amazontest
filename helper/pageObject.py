from values import strings

class Guest:

    def __init__(self, driver):
        self.driver = driver

    def guestJourney(self):
        # search item
        self.driver.myDriver.find_element_by_id(strings.search_box).send_keys(strings.search_item)
        self.driver.myDriver.implicitly_wait(10)
        self.driver.myDriver.find_element_by_css_selector(strings.search_button).click()
        # select item
        self.driver.myDriver.find_element_by_xpath(strings.select_item).click()
        self.driver.myDriver.implicitly_wait(10)
        # add to basket
        self.driver.myDriver.find_element_by_id(strings.add_to_basket).click()
        self.driver.myDriver.implicitly_wait(10)
        # add to checkout
        self.driver.myDriver.find_element_by_id(strings.checkout).click()