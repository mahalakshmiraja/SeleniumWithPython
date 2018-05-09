import unittest
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class GooglemapTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        

    def testGooglemap(self):
        """Launch the web page"""
        self.browser.get('https://www.google.com/maps/')
        self.assertIn('Google Maps', self.browser.title)

        """Give the inputs"""
        source_address = "25 Linden Ave, Somerville, Massachusetts"
        destination_address = "12 Farnsworth Street, South station, Massachusetts"

        """Click the directions icon"""
        gotosDirectionsXpath = "//*[@id='searchbox-directions']"
        gotoDirectionElement= WebDriverWait(self.browser, 5).until(lambda driver: self.browser.find_element_by_xpath(gotosDirectionsXpath))
        gotoDirectionElement.click()

        """Fill the source and destination address"""
        gotoDirectionElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='sb_ifc51']/input"))
        gotoDirectionElement.send_keys(source_address)

        gotoDirectionElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='sb_ifc52']/input"))
        gotoDirectionElement.send_keys(destination_address)

        """Select the mode of transportation from the icon"""
        gotoDirectionElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='omnibox-directions']/div/div[2]/div/div/div[1]/div[2]/button/div[1]"))
        gotoDirectionElement.click()
        
        """Condition to check time display"""
        gotoDirectionElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[1]/div[1]/span[1]"))
        if gotoDirectionElement.is_displayed():
            print("Success ! Estimated time is displayed in GoogleMaps")
        else:
            print("Sorry, Estimated time not displayed in GoogleMaps")
        

        """Condition to check Detailed route display"""
        gotoDirectionElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[2]/div[1]/div[4]/button"))
        gotoDirectionElement.click()
        gotoDirectionElement= WebDriverWait(self.browser, 10).until(lambda driver: self.browser.find_element_by_xpath("//*[@id='group_0_1']/span[2]/div/button"))
        if gotoDirectionElement.is_displayed():
            print("Success ! Instructions for the route is displayed")
        else:
            print("sorry, Instructions for the route is not displayed")


        gotoDirectionElement= WebDriverWait(self.browser, 10).until(lambda driver: 1==2)
        


if __name__ == '__main__':
    unittest.main()