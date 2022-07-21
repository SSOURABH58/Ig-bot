from urllib.request import urlretrieve

from selenium import webdriver
from zipfile import ZipFile
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

username = "2days_leonardo"
password = "Leonardo1522"
totag = ""

def ext():
    file_name = "chromedriver_win32.zip"
    try:
        with ZipFile(file_name, 'r') as zip:
            zip.extractall()
    except:
        print("noneed")
ext()
browser = webdriver.Chrome()

def login():

    browser.get(('https://www.instagram.com/accounts/login/?hl=en'))
    sleep(3)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
    sleep(5)


def copypost():
    browser.get(('https://www.instagram.com/explore/?hl=en'))
    sleep(4)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div[1]/div/div[1]/div[1]').click();
    sleep(4)
    totag = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/a').get_attribute('title')
    print(totag)
    f=True
    while(f):
        try:
            img = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/div[1]/img').get_attribute('src')
            f=False
        except:
            try:
                img = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[2]/div/div/div/div/ul/li[1]/div/div/div/div/div[1]/img').get_attribute('src')
                f = False
            except:
                try:
                    img=browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/img').get_attribute('src')
                    f = False
                except:
                    try:
                        img=browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[2]/div/div/div/div/ul/li[1]/div/div/div/div/div[1]/div/div/video').get_attribute('src')
                        f = False
                    except:
                        f = True
                        browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()

    urlretrieve(str(img), "img.jpg")
    print(img)



def close():
    browser.close()
#login()
#copypost()

