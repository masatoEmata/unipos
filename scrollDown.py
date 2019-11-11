
#ページの最下部へ移動
import json,os

from getData import GetData
from writeCsv import WriteCsv
from uploadCSVtoBigquery import UploadCSVtoBigquery
from datetime import datetime

from time import sleep
config_file = open("config.json","r")
config = json.load(config_file)

class ScrollDown:
    def __init__(self,driver):
        self.driver = driver
        config_file = open("config.json","r")
        config = json.load(config_file)
        self.file_path = config["file_path"]
        
        
    def scroll(self):
        def getup(getDataLength):
            # get data
            data = GetData(self.driver,getDataLength).get()
            getDataLength = len(data)
            # write CSV
            today = datetime.now().strftime("%Y%m%d")
            writeTime = datetime.now().strftime("%Y%m%d%H%M%S")
            table_name = "unipos_"+today
            file  = self.file_path+"unipos_"+writeTime+".csv"
            WriteCsv(data, file).write()
            sleep(5)
            UploadCSVtoBigquery(table_name,file)
            os.remove(file)
            print("remove"+file)
            return getDataLength
            
        max_position = self.driver.execute_script("return document.body.scrollHeight")
        current_position = config["first_current_position"]
        speed = config["speed"]
        
        getDataLength = 0
        while current_position < max_position:
            print(current_position , max_position)
            self.driver.execute_script("window.scrollTo(0, "+str(current_position)+");")
            current_position += speed

            #リスクヘッジのため都度データ取得
            if current_position % 10000 <= speed:
                print("getDataLength:",getDataLength)
                getDataLength += getup(getDataLength)
            if config["test"] != "True":
                max_position = self.driver.execute_script("return document.body.scrollHeight")
                if current_position >= max_position:
                    sleep(5)
                    max_position = self.driver.execute_script("return document.body.scrollHeight")
            else:
                max_position = 20000
        #残分処理
        getup(getDataLength)