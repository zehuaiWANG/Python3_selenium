from selenium import webdriver
import time
print("the first")
driver=webdriver.Firefox(executable_path="geckodriver")
driver.get("https://cas.sustc.edu.cn/cas/login?service=http%3A%2F%2Fsakai.sustc.edu.cn%2Fportal%2Flogin")
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("******")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("****")
driver.find_element_by_name("submit").click()
time.sleep(10)
driver.find_element_by_xpath("//li[2]/a/span[2]").click()
time.sleep(15)
driver.switch_to.frame("Main34bf84e4xcb5dx4724x80c4xb3a4ef48cde1")
driver.find_element_by_css_selector("a.icon.search > span").click()
time.sleep(10)
end1_31 =[]
for n in range(11613033,11613034):
     if((n%100 >= 1) and (n%100 <= 33)):
          end1_31.append(n)
for n in end1_31:
    driver.find_element_by_id("searchinput").clear()
    driver.find_element_by_id("searchinput").send_keys(n)
    driver.find_element_by_id("id1e").click()
    driver.find_element_by_id("id1e")
    time.sleep(5)
    driver.find_element_by_xpath("//div[@id='fullWidth']/div[4]/div/a/img").screenshot(str(n)+'.png')
