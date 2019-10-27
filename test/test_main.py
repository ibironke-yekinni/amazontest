from setup import WebDriver
from helper.pageObject import Guest
import unittest
class MainTest(unittest.TestCase):

    def setUp(self):
        self.browser = WebDriver()
        self.browser.fetchUrl()

    def tearDown(self):
        self.browser.shutdown()

    def test_buy_item(self):
        buyItem = Guest(self.browser)
        buyItem.guestJourney()
