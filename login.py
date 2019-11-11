import os,json
from selenium import webdriver

class Login:
    def __init__(self,driver):
        self.driver = driver
    def do(self):
        config_file = open("..\\credential\\unipos_account.json","r")
        config = json.load(config_file)
        elms = self.driver.find_elements_by_class_name("login_input")
        elms[0].send_keys(config["id"])
        elms[1].send_keys(config["pass"])
        elm = self.driver.find_element_by_class_name("login_btn")
        elm.click()
