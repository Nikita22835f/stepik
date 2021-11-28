from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

n1 = browser.find_element_by_id("num1")
n2 = browser.find_element_by_id("num2")

n1 = int(n1.text)
n2 = int(n2.text)

select = Select(browser.find_element_by_class_name("custom-select"))
select.select_by_value(str(n1 + n2))

send_button = browser.find_element_by_class_name("btn-default")
send_button.click()


time.sleep(1)
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text.split(": ")[-1])
browser.quit()
