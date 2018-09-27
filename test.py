from needle.cases import NeedleTestCase
from needle.driver import NeedlePhantomJS, NeedleChrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BBCNewsTest(NeedleTestCase):
   
    def setup(self):
        current_url = self.driver.current_url

    def wait(self, url):
        WebDriverWait(self.driver, 100).until(EC.url_changes(url))

    @classmethod
    def get_web_driver(cls):
        return NeedleChrome()
    
    def test_login(self):
        current_url = self.driver.current_url
        self.driver.get('http://scrum.swiftkind.com/')
        self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys('admin')
        self.driver.find_element_by_xpath ("//input[@placeholder='Password']").send_keys('sng55wD8eTRa')
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.wait(self.current_url)

    def test_masthead(self):
        current_url = self.driver.current_url
        self.wait(current_url)
        self.assertScreenshot('.ng-star-inserted', 'ng-star-inserted')