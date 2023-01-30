import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import XLUtility

uname = input('Enter User Name: ')
pword = input('Enter Your Password: ')


serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")  #Enter Driver Location here post extracting it.

driver = webdriver.Chrome(service=serv_obj) #creation of service object

driver.get('https://services.gst.gov.in/services/login')  #It fetches GST Website
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(uname)
driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys(pword)
time.sleep(20) #Time to enter CAPTCHA
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@role='button'][normalize-space()='Search Taxpayer']").click()
driver.find_element(By.XPATH,"//a[@data-ng-href='//services.gst.gov.in/services/auth/searchtp']").click()
time.sleep(10)

file = 'C:\\Users\\abc\\xyz\\qwe\\GST\\GSTIn.xlsx'
#Enter Location of file in which details of GSTIN is there, make sure there is '\\' as shown above

row = XLUtility.getRowCount(file,'data')

for r in range(2,row+1):
                read=XLUtility.readData(file,'data',r,1)
                driver.find_element(By.XPATH,"//input[@id='for_gstin']").send_keys(read)
                driver.find_element(By.XPATH,"//button[@id='lotsearch']").click()
                time.sleep(5)
                legalName = driver.find_element(By.XPATH,"//body/div/div/div/div/div/div/form[@name='searchtax']/div[@id='lottable']/div[2]/div[1]/div[1]/p/strong").text
                time.sleep(5)
                status = driver.find_element(By.XPATH,"//p[@data-ng-bind='trans.LBL_GSTIN_STAT']/../p/strong").text
                writeNB = XLUtility.writeData(file, 'data', r, 2, str(legalName))
                writeStatus = XLUtility.writeData(file, 'data', r, 3, str(status))
                driver.find_element(By.XPATH, "//input[@id='for_gstin']").clear()
                time.sleep(5)


for r in range(2,row+1):
    read1 = XLUtility.readData(file, 'data', r, 2)
    read2 = XLUtility.readData(file, 'data', r+1, 2)
    if read1 == read2:
        writeNB1 = XLUtility.writeData(file,'data',r+1,2,'Invalid GST Number')
        writeStatus1 = XLUtility.writeData(file, 'data', r+1, 3, 'Invalid GST Number')
    else:
        pass



