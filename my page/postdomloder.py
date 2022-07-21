from urllib.request import urlretrieve
from selenium import webdriver
from time import sleep
from zipfile import ZipFile
from selenium.webdriver.chrome.options import *
import autoit

def ext():
    file_name = "chromedriver_win32.zip"
    try:
        with ZipFile(file_name, 'r') as zip:
            zip.extractall()
    except:
        print(" some think went rong ")
ext()

username = "2days_leonardo"
passwd = "Leonardo1522"
driverpth = "chromedriver.exe"
photopath = "C:\Spython\img.jpg" #examp "C:\\Users\\alire\\PycharmProjects\\instagrambot2\\logo.png"
phototext = "#Repost #photoshop #digitalportrait post from @"+"silviemahdal_art"+" \n #duende_arts_help #art #artist #sketch #illustration #draw #drawing #pencil #beautiful #sketchbook #picture #artista #ink #tattoos #artwork #instagram #blackandwhiteart #design #blackandwhite #ritratto #creative #graphic #photography #disney #disegno #portrait"
pages= ["silviemahdal_art"]
viral_list = ["https://www.instagram.com/p/B6YdT0GFoM8/"]
dowmlodedP=[[]]

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

def login():
    driver.get("https://www.instagram.com/accounts/login/?hl=tr")
    sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(username)
    sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(passwd)
    sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div").click()
    sleep(6)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/button').click()
    sleep(3)

def avrajLikeCounter(pagename):
    likesum = 0.0
    postcount=10
    driver.get("https://www.instagram.com/"+pagename+"/")
    sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div/div/section/div/div[2]/div[4]/button/div').click()
    except:
        pass
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article[1]/div/div/div[1]/div[1]/a/div[1]').click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
    #/html/body/div[5]/div[1]/div/div/a[2] -- not loged in
    #/html/body/div[4]/div[1]/div/div/a[2] -- loged in
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
    sleep(1)
    loopv=postcount
    while (loopv>=1):
        sleep(4)
        temp = 0
        num = 0
        templen = 0
        try:
            temp = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/section[2]/div/div/a/span').text
#//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/a/span
            #/html/body/div[5]/div[2]/div/article/div[2]/section[2]/div/div/a/span
        except:
            temp = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/section[2]/div/div[2]/a[2]/span').text
            #//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/a/span
            #/html/body/div[5]/div[2]/div/article/div[2]/section[2]/div/div[2]/a[2]/span
        temp = str(temp)

        templen = len(temp)
        print("\n lngth : "+str(templen))
        for n in temp:
            if(n != ','):
                num+=int(n)*pow(10,templen-1)
            else:
                num /= 10
            templen-=1

        likesum = likesum + num
        print(str(loopv)+" : "+str(temp)+" num : "+ str(num))
        try:
            driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
        except:
            try:
                driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
            except:
                driver.find_element_by_xpath('/html/body/div[5]/button[1]').click()
                # /html/body/div[5]/button[1]
                sleep(1)
                driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div[3]/article[2]/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()
                # //*[@id="react-root"]/section/main/div/div[3]/article[2]/div[1]/div/div[1]/div[1]/a/div[1]/div[2]
        loopv-=1
    print("\n Total likes : "+str(likesum)+"\n Avrage like : "+str(likesum/postcount)+"\n Likes neadded to post : "+str((likesum/postcount)*1.5))
    return ((likesum/postcount)*1.5)
def viralfinder(pagename,like_want,serch_amount):
        driver.get("https://www.instagram.com/" + pagename + "/")
        sleep(3)
        try:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div/div/section/div/div[2]/div[4]/button/div').click()
        except:
            pass
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article[1]/div/div/div[1]/div[1]/a/div[1]').click()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
        driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
        sleep(1)
        while (serch_amount >= 1):
            sleep(3)
            temp = 0
            num = 0
            templen = 0
            postL=driver.current_url
            try:
                temp = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/section[2]/div/div/a/span').text
            except:
                temp = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/section[2]/div/div[2]/a[2]/span').text
                #/html/body/div[5]/div[2]/div/article/div[2]/section[2]/div/div/a/span
            temp = str(temp)
            templen = len(temp)
            for n in temp:
                if (n != ','):
                    num += int(n) * pow(10, templen - 1)
                else:
                    num /= 10
                templen -= 1
            if (num >= like_want ):
                viral_list.append(str(postL))
                print(str(postL))
            print(str(serch_amount) + " : " + str(temp) + " num : " + str(num))
            try:
                driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()
            except:
                try:
                    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
                except:
                    driver.find_element_by_xpath('/html/body/div[5]/button[1]').click()
                    sleep(1)
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article[2]/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()
            serch_amount -= 1

def post_domw(postlink,diractry):
    driver.get(str(postlink))
    sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div/div/section/div/div[2]/div[4]/button/div').click()
    post=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[1]/div/div/div[2]/div/div/div/div/ul/li[1]/div/div/div/div/div[1]/div/video').get_attribute('src')
    tag=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[1]/h2/a').text
    urlretrieve(str(post), diractry+".mp4")
    print(str(tag))

def reposter(post,caption,tag):
    #cant  post videos
    login()
    driver.get('https://www.instagram.com/2days_leonardo/')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span').click()
    sleep(1.5)
    autoit.win_active("Open")  # open can change by your os language if not open change that
    sleep(2)
    autoit.control_send("Open", "Edit1", post)
    sleep(1.5)
    autoit.control_send("Open", "Edit1", "{ENTER}")
    sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys(caption)
    sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    sleep(4)

def dockmunt():
    getpage= "pip/pagelist.txt"
    pagelike= "pip/pagelikes.;txt"
    fg=open(getpage,"r")
    fp=open(pagelike,"a")
    while():
        pagename = fg.read(1)

def auto_fallow(post):
    driver.get(post)

viralfinder("silviemahdal_art",4000,30)