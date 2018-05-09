import unittest
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

class BehindwoodsTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testBehindwoods(self):
        gotoBehindwoodsXpath = "//a[@href='//www.raaga.com/tamil']"
        self.browser.get('https://www.raaga.com')

        gotoBehindwoodsElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath(gotoBehindwoodsXpath))
        gotoBehindwoodsElement.click()
        gotoBehindwoodsElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//p[@id='lang_name_dv']"))
        #gotoBehindwoodsElement= WebDriverWait(self.browser, 5)
        gotoBehindwoodsElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='language-notification']/div/div/div[2]/div[2]/div[1]/a"))
        gotoBehindwoodsElement.click()
        gotoBehindwoodsElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//a[@id='top10_lnk_lft']"))
        gotoBehindwoodsElement.click()
        gotoBehindwoodsElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='top10songs_playbtn_div']"))
        gotoBehindwoodsElement.click()
        gotoBehindwoodsElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='starting_time']"))
        gotoBehindwoodsElement= WebDriverWait(self.browser, 20).until(lambda driver: gotoBehindwoodsElement.text == "00:15")

if __name__ == '__main__':
    unittest.main(verbosity=2)