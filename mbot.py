from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import autoit
import time
import bot
bot.ext()
username = "2days_leonardo"
passwd = "Leonardo1522"
driverpth = "chromedriver.exe"
photopath = "C:\Spython\img.jpg" #examp "C:\\Users\\alire\\PycharmProjects\\instagrambot2\\logo.png"
phototext = "#Repost #photoshop #digitalportrait drawn by @"+bot.totag+" \n #duende_arts_help #art #artist #sketch #illustration #draw #drawing #pencil #beautiful #sketchbook #picture #artista #ink #tattoos #artwork #instagram #blackandwhiteart #design #blackandwhite #ritratto #creative #graphic #photography #disney #disegno #portrait"

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
#mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(executable_path=driverpth,options=options)
driver.get("https://www.instagram.com/accounts/login/?hl=tr")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(username)
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(passwd)
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div").click()
time.sleep(6)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/button').click()
time.sleep(3)

def temp():
    driver.get('https://www.instagram.com/2days_leonardo/')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span').click()
    time.sleep(1.5)
    autoit.win_active("Open") #open can change by your os language if not open change that
    time.sleep(2)
    autoit.control_send("Open", "Edit1", photopath)
    time.sleep(1.5)
    autoit.control_send("Open", "Edit1", "{ENTER}")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys(phototext)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(4)
    driver.close()

temp()