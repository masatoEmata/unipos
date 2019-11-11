from datetime import datetime
from selenium.webdriver.common.by import By
from formatText import FormatText
from selenium.common.exceptions import NoSuchElementException

class GetData:
    def __init__(self, driver,getDataLength):
        self.driver = driver
        self.getDataLength = getDataLength

    def get(self):
        target = self.driver.find_element_by_class_name("main")
        # .find_element_by_class_name("timeline-body").find_element_by_class_name("cards")
        elements = target.find_elements_by_class_name("card  ")
        data = []
        cnt = 0
        timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        error_count = 0
        for element in elements[self.getDataLength:]:
            try:
                card_left = element.find_element_by_class_name("card_left")
                sender = card_left.find_element_by_class_name("card_id").text
                post_time  = "2019/"+card_left.find_element_by_class_name("card_time").text+":00"
                message = card_left.find_element_by_class_name("card_body").text
                message  = FormatText(message).mySubstrings()
                card_right = element.find_element_by_class_name("card_right")
                point = card_right.find_element_by_class_name("card_pointTo").text.strip("+")
                receiver = card_right.find_element_by_class_name("card_nameTo").text

                data.append([
                    timestamp,
                    post_time,
                    sender,
                    receiver,
                    point,
                    message
                ])
            except NoSuchElementException:
                error_count += 1
                if error_count>15:
                    print("error count > 15")
                    break
                pass
        print(data)
        return data
