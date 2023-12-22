import unittest
from selenium import webdriver

class TestCalculatorUI(unittest.TestCase):
    def setUp(self):
        # Replace with the path to your WebDriver
        #self.driver = webdriver.Firefox(executable_path='/path/to/geckodriver')
        self.driver = webdriver.Chrome(executable_path='D:\\tools\webdriver\\chromedriver-win64\\chromedriver.exe')

    def tearDown(self):
        self.driver.quit()

    def test_index(self):
        self.driver.get('http://localhost:5000')
        buttons = self.driver.find_elements_by_tag_name('button')
        self.assertEqual(len(buttons), 12)  # Adjust this based on the number of buttons you have

        # Test a button
        button = self.driver.find_element_by_xpath("//button[normalize-space()='1']")
        button.click()
        operation = self.driver.find_element_by_id('operation')
        self.assertEqual(operation.get_attribute('value'), '1')

if __name__ == '__main__':
    unittest.main()