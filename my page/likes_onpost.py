import time
from time import sleep
from zipfile import ZipFile

from selenium import webdriver

def ext():
    file_name = "chromedriver_win32.zip"
    try:
        with ZipFile(file_name, 'r') as zip:
            zip.extractall()
    except:
        print("noneed")
ext()
driver = webdriver.Chrome('C:\python\coldemails\chromedriver.exe')
browser = driver
def login():
    username = "table_charger"
    password = "bot1522"
    browser.get(('https://www.instagram.com/accounts/login/?hl=en'))
    sleep(3)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    sleep(5)

login()
driver.get('https://www.instagram.com/p/CGKvl0dl843/?utm_source=ig_web_copy_link')
time.sleep(3)
userid_element = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[2]/div/div/button').click()
time.sleep(2)
#//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/a
#//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/button/span
# here, you can see user list you want.
# you have to scroll down to download more data from instagram server.
# loop until last element with users table view height value.

users = []

height = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div").value_of_css_property("padding-top")
#/html/body/div[4]/div/div[2]/div/div
match = False
while match==False:
    lastHeight = height

    # step 1
    elements = driver.find_elements_by_xpath("//*[@id]/div/span/a")

    # step 2
    for element in elements:
        if element.get_attribute('title') not in users:
            users.append(element.get_attribute('title'))

    # step 3
    driver.execute_script("return arguments[0].scrollIntoView();", elements[-1])
    time.sleep(1)

    # step 4
    height = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div").value_of_css_property("padding-top")
    print(height)
    #/html/body/div[4]
    if lastHeight==height:
        match = True
f=open("record/weaktimes.txt")
f.write(users)
print(users)
print(len(users))
driver.quit()