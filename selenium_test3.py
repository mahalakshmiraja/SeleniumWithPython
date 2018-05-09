import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class amazonShopping(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def testCart(self):
        browser = self.browser
        browser.get("https://www.amazon.com/")
        AllDepartmentsXpath = "//*[@id='nav-link-shopall']/span[2]"
        browser.find_element_by_xpath(AllDepartmentsXpath).click()
        browser.find_element_by_xpath("//*[@id='a-page']/div[2]/div/div[2]/div[4]/div/a[1]").click()
        author = browser.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
        author.click()
        author.send_keys("paulo coelho books")
        browser.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
        browser.find_element_by_xpath("//*[@id='result_0']/div/div/div/div[2]/div[1]/div[1]/a/h2").click()
        browser.find_element_by_xpath("//*[@id='bbop-check-box']").click()
        browser.find_element_by_xpath("//*[@id='add-to-cart-button']").click()

        halt= WebDriverWait(self.browser, 10).until(lambda driver: 1==2)
        #browser.find_element_by_xpath("//*[@id='bbop-check-box']").click()
        #author.text("The Alchemist")
        #src  = browser.page_source
        #print (src)


if __name__ == '__main__':
    unittest.main()

   