from selenium.common.exceptions import NoSuchElementException

try:
    raise NoSuchElementException
except NoSuchElementException:
    print("error")