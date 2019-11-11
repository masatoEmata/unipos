from login import Login
from selenium import webdriver
from scrollDown import ScrollDown
#from getData import GetData
#from writeCsv import WriteCsv
#from uploadCSVtoBigquery import UploadCSVtoBigquery
from time import sleep
#from datetime import datetime

#login
driver = webdriver.Chrome()
driver.get("https://unipos.me/login")
Login(driver).do()
# scroll
sleep(20)
driver.get("https://unipos.me/all")
ScrollDown(driver).scroll()
## get data
#data = GetData(driver).get()
## write CSV
#today = datetime.now().strftime("%Y%m%d")
#name = "unipos_"+today
#WriteCsv(data, name+".csv").write()
#sleep(10)
#UploadCSVtoBigquery(name)
