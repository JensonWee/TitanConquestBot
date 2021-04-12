
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import ctypes  # An included library with Python install.

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--window-size=1920,1080');
options.headless = True

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
driver.get("https://titanconquest.com/")

def alertMSG(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def loadPage():
    time.sleep(3);
def sleepShort():
    time.sleep(1);
def logIn():
    #Remove Notification
    #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,  "//button[text()='No Thanks']")))
    loadPage();
    notiButton = driver.find_elements_by_xpath("//button[text()='No Thanks']");
    if len(notiButton) > 0 :
        notiButton[0].click();
    time.sleep(1);
    loginBar = driver.find_element_by_xpath("//div[text()='Login to your Account']");
    loginBar.click();
    loadPage();
    # Log in
    userName = driver.find_element_by_name("username");
    userName.send_keys(username);
    passWord = driver.find_element_by_name("password");
    passWord.send_keys(password);
    submitBtn = driver.find_element_by_xpath("//input[@type='submit']");
    submitBtn.click();
    loadPage();


def printStatus():
    driver.get("https://titanconquest.com/index.php");
    print(10*"=" + "Home Page" + 10*"=");
    heroDetails = driver.find_elements_by_xpath("//div[@class='card']//*//div[@class='item-title']");
    heroDetails2 = driver.find_elements_by_xpath("//div[@class='card']//*//div[@class='item-after']");
    print(5*"=" + "Active Hero" + 5*"=")
    activeHeroText = ["Guardian : ", "SubClass : ", "Game Progress", "Daily Rewards"]
    for a in range(2):
        print(activeHeroText[a] + heroDetails[a].text.strip() + " | " + heroDetails2[a].text.strip());
    print(activeHeroText[2] + " : " + heroDetails2[2].text.strip());
    print(activeHeroText[3] + " : " + heroDetails2[3].text.strip());
    print(20*"=" );

def setLuckDay():
    driver.get_screenshot_as_file('setLuck.png');
    checkLuc = driver.find_elements_by_xpath('''//*[starts-with(.,"It's you")]''');
    if len(checkLuc) > 0:
        sleepShort();
        if luckyday.lower() == "xp" or luckyday.lower() == "lp":
            print("Setting : " + luckyday.lower())
            setLuckBar = driver.find_element_by_xpath("//*[text()='+ "+luckyday.upper()+"']");
            setLuckBar.click();
        elif luckyday.lower() == "drachma":
            print("Setting : " + luckyday.lower())
            setLuckBar = driver.find_element_by_xpath("//*[text()='+ Drachma']");
            setLuckBar.click();
        YesBtn = driver.find_element_by_xpath('//*[text()="Yes"]');
        sleepShort();
        YesBtn.click();
        loadPage();
    else:
        print("No Luck Day");
def goPatrol():
    patrolBar = driver.find_element_by_xpath("//*[starts-with(.,'Patrol')]");
    patrolBar.click();
    loadPage();
    setLuckDay();
    loadPage()
    showHide = driver.find_element_by_xpath("//*[starts-with(.,'Show/')]");
    showHide.click();
    sleepShort();

def grindPatrol(arg1):
    location = driver.find_element_by_xpath('//*[starts-with(.,"Patrolling")]');
    print("Current Location : " + location.text.strip().replace("Patrolling ", ""));
    print(10*'=');
    if(arg1):
        for i in range(5000):
            selectMob1();
            sleepShort()
            mobDeath = False;
            while mobDeath == False:
                if fightMob():
                    mobDeath = True;
            print(10*'=');
            loadPage();
    else:
        sleepShort();
        selectMob1();
        sleepShort()
        mobDeath = False;
        while mobDeath == False:
            if fightMob():
                mobDeath = True;
        print(10*'=');
        loadPage();


def selectMob1():
    driver.get_screenshot_as_file('capture.png');
    mobBar = driver.find_elements_by_xpath("//ul[@id='enemyList']//*//div[@class='item-content']");
    mobName = driver.find_elements_by_xpath("//ul[@id='enemyList']//*//div[@class='item-content']//div//div[@class='item-title']");
    if(mobName[1].text.startswith('Sacred')):
        print("Selecting Mob : "+mobName[2].text);
        mobBar[2].click();
    else:
        print("Selecting Mob : "+mobName[1].text);
        mobBar[1].click();

def reRoute():
    driver.get_screenshot_as_file('capture.png');
    goToBar = driver.find_elements_by_xpath("//*[starts-with(.,'Go to')]");
    goToBar[2].click();
    print("Rerouting.....");

def selectMob(Mob,arg2):
    driver.get_screenshot_as_file('capture.png');
    mobBar = driver.find_elements_by_xpath("//div[@class='item-title'][starts-with(text(),'"+Mob+"')]/..");
    mobName = driver.find_elements_by_xpath("//ul[@id='enemyList']//*//div[@class='item-content']//div//div[@class='item-title']");
    lookAroundBar = driver.find_element_by_xpath("//*[starts-with(.,'Look around')]/..");
    print("Finding Mob : "+Mob);
    if len(mobBar) > 0:
        mobBar[0].click();
        sleepShort();
        return True;
    else:
        lookAroundBar.click();
        loadPage();
        return False;

def checkDefeatedMob():
    defeatBar = driver.find_elements_by_xpath("//*[starts-with(.,'Back to')]");
    if len(defeatBar) > 0:
        defeatBar[0].click()
        return True;
    else:
        return False;
def mobStatus():
    mobName = driver.find_elements_by_xpath("//div[@class='center sliding']")[2].text.strip();
    print("Mob name : " + mobName);

def primaryAttack():
    primaryAtkBar = driver.find_elements_by_xpath("//*[starts-with(.,'Primary')]");
    if(len(primaryAtkBar) > 0 ):
        print("Primary Attacking...");
        sleepShort()
        primaryAtkBar[0].click();
    else:
        primaryAtkBar = driver.find_elements_by_xpath("//*[starts-with(.,'Hit it')]");
        print("Hitting it...");
        sleepShort()
        primaryAtkBar[0].click();

def checkDeath():
    respawnBar = driver.find_elements_by_xpath("//*[starts-with(.,'Respawn where')]");
    if len(respawnBar) > 0 :
        print("You died.");
        respawnBar[0].click();
        return True;
    else:
        return False;
def fightMob():
    if (checkDefeatedMob()):
        print("Mob defeated.")
        return True
    else:
        primaryAttack();
        sleepShort();
        if checkDeath():
            return True
def grindBounty(arg1, Mob, arg2):
    location = driver.find_element_by_xpath('//*[starts-with(.,"Patrolling")]');
    print("Current Location : " + location.text.strip().replace("Patrolling ", ""));
    print(10*'=');
    found = False;
    if(arg1):
        for i in range(5000):
            counter = 0;
            found = False;
            while found == False:
                found = selectMob(Mob,arg2);
                counter+=1;
                if(arg2 == True and counter == 10):
                    reRoute();
                    loadPage();
            sleepShort()
            sleepShort()
            mobDeath = False;
            while mobDeath == False:
                if fightMob():
                    mobDeath = True;
            print(10*'=');
            loadPage();
    else:
        sleepShort();
        while found == False:
            found = selectMob(Mob,arg2);
            sleepShort()
        mobDeath = False;
        while mobDeath == False:
            if fightMob():
                mobDeath = True;
        print(10*'=');
        loadPage();


username = ""
password = ""
luckyday = "drachma" #xp/lp/drachma
logIn();
printStatus();
goPatrol();
#grindBounty(True, "Nymph Leader", True);
grindPatrol(True);
alertMSG('Task', 'Completed!', 1)
driver.quit();