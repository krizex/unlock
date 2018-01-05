#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def main():
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:8910',
        desired_capabilities=DesiredCapabilities.PHANTOMJS)

    driver.get('https://citrix.service-now.com/unlock.do')
    driver.find_element_by_id('userId').send_keys('yangqi')
    driver.find_element_by_xpath("//input[@value='Submit']").click()
    driver.save_screenshot('click.png')
    driver.quit()


if __name__ == '__main__':
    main()
