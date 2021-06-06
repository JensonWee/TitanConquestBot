
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import ctypes  # An included library with Python install.
import os, re


def printStartMsg():
    print("======================Titan Conquest Bot v3.3 =========================")
    print("Written by JensonWee(GitHub)")
    print("Free Usage for all :)")
    print ("=" * 70)

def cleanUpProcess():
    print("=============Process Clean up==================")
    os.system('taskkill /F /IM "chrome.exe"')
    os.system('taskkill /F /IM "chromedriver.exe"')
    # os.system('taskkill /F /IM "firefox.exe"')
    # os.system('taskkill /F /IM "geckodriver.exe"')
    print("="*10)


def waitObject(xpath):
    try:
        element_present = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(driver, 10).until(element_present)
        return True
    except:
        return False

def objectVisible(xpath):
    return driver.find_element_by_xpath(xpath).is_displayed()

def waitShortObject(xpath):
    try:
        element_present = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(driver, 3).until(element_present)
        return True
    except:
        return False


cleanUpProcess()
options = webdriver.ChromeOptions()
#options = webdriver.FirefoxOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--window-size=1920,1080')
options.headless = True
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
#driver = webdriver.Firefox(executable_path='geckodriver.exe', options=options)
def loadPage():
    time.sleep(2)
def sleepShort():
    time.sleep(0.5)

def getElements(xpath):
    return driver.find_elements_by_xpath(xpath)
def getElement(xpath):
    return driver.find_element_by_xpath(xpath)

def logIn():
    #Remove Notification
    driver.get("https://titanconquest.com/")
    loadPage()
    notiButton = getElements("//button[text()='Later']")
    if len(notiButton) > 0 :
        notiButton[0].click()
    time.sleep(1)
    loginBar = getElement("//div[text()='Login to your Account']")
    loginBar.click()
    loadPage()
    # Log in
    userName = driver.find_element_by_name("username")
    userName.send_keys(username)
    passWord = driver.find_element_by_name("password")
    passWord.send_keys(password)
    submitBtn = getElement("//input[@type='submit']")
    submitBtn.click()
    loadPage()


def printStatus():
    driver.get("https://titanconquest.com/index.php")
    print(10*"=" + "Home Page" + 10*"=")
    heroDetails = driver.find_elements_by_xpath("//div[@class='card']//*//div[@class='item-title']")
    heroDetails2 = driver.find_elements_by_xpath("//div[@class='card']//*//div[@class='item-after']")
    print(5*"=" + "Active Hero" + 5*"=")
    activeHeroText = ["Guardian : ", "SubClass : ", "Game Progress", "Daily Rewards"]
    for a in range(2):
        print(activeHeroText[a] + heroDetails[a].text.strip() + " | " + heroDetails2[a].text.strip())
    print(activeHeroText[2] + " : " + heroDetails2[2].text.strip())
    print(activeHeroText[3] + " : " + heroDetails2[3].text.strip())
    print(20*"=" )

def setLuckDay():
    driver.get_screenshot_as_file('./Screenshot/setLuck.png')
    checkLuc = driver.find_elements_by_xpath('''//*[starts-with(.,"It's you")]''')
    print('Checking for Lucky Day...')
    if len(checkLuc) > 0:
        print("Luck Day Set")
        sleepShort()
        if luckyday.lower() == "xp" or luckyday.lower() == "lp":
            print("Setting : " + luckyday.lower())
            setLuckBar = driver.find_element_by_xpath("//*[text()='+ "+luckyday.upper()+"']")
            setLuckBar.click()
        elif luckyday.lower() == "drachma":
            print("Setting : " + luckyday.lower())
            setLuckBar = driver.find_element_by_xpath("//*[text()='+ Drachma']")
            setLuckBar.click()
        YesBtn = driver.find_element_by_xpath('//*[text()="Yes"]')
        sleepShort()
        YesBtn.click()
        loadPage()
    else:
        print("No Luck Day")
def goPatrol():
    driver.get_screenshot_as_file('./Screenshot/goPatrol.png')
    patrolBar = "//*[starts-with(.,'Patrol')]"
    goBackBar = "//*[starts-with(.,'Go back to')]/../.."
    if(len(getElements(patrolBar)) > 0):
        getElements(patrolBar)[0].click()
    else:
        html = getElements("//div[@class='page-content']")
        driver.execute_script('arguments[0].scrollTop = 1080', html[2])
        print("Clicking Go Back To...")
        if waitObject(goBackBar):
            getElements(goBackBar)[0].click()
    setLuckDay()
    showHide = driver.find_elements_by_xpath("//*[starts-with(.,'Show/')]")
    findBounty = driver.find_elements_by_xpath("//*[@style='display: none']//*[starts-with(text(),'Bounty')]")
    if len(findBounty) == 0:
        if len(showHide) > 0:
            showHide[0].click()
        sleepShort()

def collectPostMaster():
    acropolisBar = "//div[text()='Go back to The Acropolis']/.."
    postMasterBar = "//div[contains(text(), 'Postmaster')]"
    blackCommissaryBar = "//div[contains(text(), 'Black Commissary')]"
    collectAllBtn = "//*[text()='Collect All']"
    okBtn = "//*[text()='OK']"
    homeBtn = "//div[text()='Home']"
    time.sleep(3)
    if waitObject(acropolisBar):
        print("Clicking Go Back To...")
        driver.find_element_by_xpath(acropolisBar).click()
    if waitObject(blackCommissaryBar):
        html = getElements("//div[@class='page-content']")
        driver.find_element_by_xpath(postMasterBar).click()
        driver.execute_script('arguments[0].scrollTop = 1080', html[1])
        driver.find_element_by_xpath(postMasterBar).click()
        if waitObject(collectAllBtn):
            driver.find_element_by_xpath(collectAllBtn).click()
            time.sleep(3)
            driver.find_element_by_xpath(okBtn).click()
            time.sleep(1)
        driver.find_element_by_xpath(homeBtn).click()
        time.sleep(5)
def grindPatrol(arg1):
    location = driver.find_element_by_xpath('//*[starts-with(.,"Patrolling")]')
    print("Current Location : " + location.text.strip().replace("Patrolling ", ""))
    print(10*'=')
    if(arg1):
        for i in range(5000):
            setLuckDay()
            selectMob1()
            sleepShort()
            mobDeath = False
            while mobDeath == False:
                if fightMob():
                    mobDeath = True
            print(10*'=')
            loadPage()
    else:
        sleepShort()
        selectMob1()
        sleepShort()
        mobDeath = False
        while mobDeath == False:
            if fightMob():
                mobDeath = True
        print(10*'=')
        loadPage()


def selectMob1():
    driver.get_screenshot_as_file('./Screenshot/selectMob1.png')
    mobBar = "//ul[@id='enemyList']//*//div[@class='item-content']"
    mobName = "//ul[@id='enemyList']//*//div[@class='item-content']//div//div[@class='item-title']"
    for i in range(10):
        if(not getElements(mobName)[i+1].text.startswith('Sacred')):
            print("Selecting Mob : "+getElements(mobName)[i+1].text)
            getElements(mobBar)[i+1].click()
            break


def reRoute():
    driver.get_screenshot_as_file('./Screenshot/reroute.png')
    goToBar = "//li[@class='widebg']//*[starts-with(.,'Go to')]"
    waitObject(goToBar)
    getElements(goToBar)[0].click()
    print("Rerouting.....")

def selectMob(Mob,arg2):
    driver.get_screenshot_as_file('./Screenshot/selectMob.png')
    mobBar = "//div[@class='item-title'][starts-with(text(),'"+Mob+"')]/.."
    mobName = driver.find_elements_by_xpath("//ul[@id='enemyList']//*//div[@class='item-content']//div//div[@class='item-title']")
    lookAroundBar = getElement("//*[starts-with(.,'Look around')]/..")
    print("Finding Mob : "+Mob)
    loadPage()
    if len(getElements(mobBar)) > 0:
        getElements(mobBar)[0].click()
        return True
    else:
        lookAroundBar.click()
        sleepShort()
        return False

def checkDefeatedMob():
    driver.get_screenshot_as_file('./Screenshot/defeated.png')
    defeatBar = "//*[starts-with(.,'Back to')]"
    if len(getElements(defeatBar)) > 0:
        getElements(defeatBar)[0].click()
        return True
    else:
        return False
def mobStatus():
    mobName = driver.find_elements_by_xpath("//div[@class='center sliding']")[2].text.strip()
    print("Mob name : " + mobName)

def primaryAttack():
    sleepShort()
    driver.get_screenshot_as_file('./Screenshot/primaryAtk.png')
    primaryAtkBar = driver.find_elements_by_xpath("//*[starts-with(.,'Primary')]/..")
    if(len(primaryAtkBar) > 0 ):
        print("Primary Attacking...")
        primaryAtkBar[0].click()
    else:
        primaryAtkBar = driver.find_elements_by_xpath("//*[starts-with(.,'Hit it')]")
        print("Hitting it...")
        sleepShort()
        primaryAtkBar[0].click()
def heavyAttack():
    sleepShort()
    driver.get_screenshot_as_file('./Screenshot/heavuAtk.png')
    heavyAtkBar = driver.find_elements_by_xpath("//*[starts-with(.,'Heavy (')]/..")
    dazedText = driver.find_elements_by_xpath("//*[contains(text(), 'DAZED')]")
    if(len(heavyAtkBar) > 0 ):
        print("Heavy Attacking...")
        if(len(dazedText) > 0) :
            sleepShort()
            primaryAttack()
        else:
            heavyAtkBar[0].click()
    else:
        heavyAtkBar = driver.find_elements_by_xpath("//*[starts-with(.,'Hit it')]")
        print("Hitting it...")
        sleepShort()
        heavyAtkBar[0].click()


def smartAttack():
    driver.get_screenshot_as_file('./Screenshot/smartAtk.png')
    shieldBar = "//div[@class='progress shield']"
    heavyAtkBar = "//*[starts-with(.,'Heavy (')]/.."
    hitAtkBar = "//*[starts-with(.,'Hit it')]"
    flareAtkBar = "//span[@class='actionimg'][starts-with(.,'Flare Bomb')]"
    primaryAtkBar = "//*[starts-with(.,'Primary')]/.."
    specialAtkBar = "//*[starts-with(.,'Special (')]/.."

    checkSpecialStatus() #Uses remedy
    if len(getElements(shieldBar)) > 0:
        if waitObject(specialAtkBar):
            print("Special Attacking...")
            getElements(specialAtkBar)[0].click()
    else:
        if len(getElements(flareAtkBar)) > 0:
            if waitObject(flareAtkBar):
                if len(getElements(flareAtkBar)) > 1:
                    print("Flare Bombing 1...")
                    getElements(flareAtkBar)[1].click()
                else:
                    print("Flare Bombing...")
                    getElements(flareAtkBar)[0].click()
        elif len(getElements(heavyAtkBar)) >0:
            if waitObject(heavyAtkBar):
                print("Heavy Attacking...")
                getElements(heavyAtkBar)[0].click()
        elif len(getElements(hitAtkBar)) > 0:
            if waitObject(hitAtkBar):
                print("Hitting it...")
                getElements(hitAtkBar)[0].click()
        elif len(getElements(primaryAtkBar)) > 0:
            if waitObject(primaryAtkBar):
                print("Primary Attacking...")
                getElements(primaryAtkBar)[0].click()
        else:
            return False

def checkSpecialStatus():
    driver.get_screenshot_as_file('./Screenshot/remedy.png')
    heartFillIcon = "//*[contains(text(), 'heart_fill')]/.."
    if(len(getElements(heartFillIcon)) > 0):
        waitObject(heartFillIcon)
        print("Uses Remedy...")
        sleepShort()
        getElements(heartFillIcon)[0].click()


def checkDeath():
    respawnBar = "//*[starts-with(.,'Respawn where')]/.."
    if len(getElements(respawnBar)) > 0 :
        print("You died.")
        waitObject(respawnBar)
        getElements(respawnBar)[0].click()
        return True
    else:
        return False
def fightMob():
    if (checkDefeatedMob()):
        print("Mob defeated.")
        return True
    elif checkDeath == True:
        print("You're instant dead.")
        return True
    else:
        smartAttack()
        sleepShort()
        if checkDeath() == True:
            return True
def grindBounty(arg1, Mob, arg2):
    location = driver.find_element_by_xpath('//*[starts-with(.,"Patrolling")]')
    print("Current Location : " + location.text.strip().replace("Patrolling ", ""))
    print(10*'=')
    mobCount = 0
    found = False
    if(arg1):
        for i in range(5000):
            counter = 0
            found = False
            while found == False:
                found = selectMob(Mob,arg2)
                counter+=1
                if(arg2 == True and counter >= 5 and found == False):
                    reRoute()
                sleepShort()
            sleepShort()
            mobDeath = False
            while mobDeath == False:
                if fightMob():
                    mobDeath = True
            print(10*'=')
            mobCount+=1
            sleepShort()
            print(Mob + " has been killed " + str(mobCount) + " times.")
    else:
        sleepShort()
        while found == False:
            found = selectMob(Mob,arg2)
            sleepShort()
        mobDeath = False
        while mobDeath == False:
            if fightMob():
                mobDeath = True
        print(10*'=')
        sleepShort()

f = open("UserOptions.txt", "r")
username = re.findall(r'\".*?\"', f.readline())[0].replace('"', '')
password = re.findall(r'\".*?\"', f.readline())[0].replace('"', '')
luckyday = re.findall(r'\".*?\"', f.readline())[0].replace('"', '')
printStartMsg()

while True:
#for i in range(1):
    try:
        logIn()
        printStatus()
        #collectPostMaster()
        goPatrol()
        #grindBounty(True, "Chiron Knight", True)
        grindPatrol(True)
    except:
        print("Run failed. Re-running....")
        cleanUpProcess()
        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        #driver = webdriver.Firefox(executable_path='geckodriver.exe', options=options)
        #print(Exception)

# logIn()
# printStatus()
# #collectPostMaster()
# goPatrol()
# grindPatrol(True)