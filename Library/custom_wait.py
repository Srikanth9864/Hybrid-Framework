
import time
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait


# Overriding Base Class of expected_conditions module
class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self, driver):
        # Overriding __call__ method present in Parent class
        # Calling __call__ method of parent class. (Re-using the parent class functionality)
        result = super().__call__(driver)
        # result will have either WebElement if the element is visible
        # or result will have bool False if the element is not visible.
        if isinstance(result, WebElement):
            # Checking if the element is enabled is the extra functionality that I am adding in child class
            return result.is_enabled()
        else:
            return False


def wait_(visibility=True, enabled=True, timeout=10, is_alert=False):
    def _func(func):
        def wrapper(*args, **kwargs):
            instance, element = args
            wait = WebDriverWait(instance.driver, timeout, poll_frequency=0.5)
            if is_alert:
                wait.until(alert_is_present(), message='Alert does not exist')
            elif visibility and enabled:
                wait.until(_visibility_of_element_located(element),
                           message=f'{element} not visible after timeout period of {timeout} seconds')
            elif visibility:
                wait.until(visibility_of_element_located(element), message = f'{element} is enabled after timeout period of {timeout} seconds')
            else:
                time.sleep(2)
                wait.until(invisibility_of_element_located(element),
                           message=f'{element} is visible after timeout period of {timeout} seconds')
            return func(*args, **kwargs)
        return wrapper
    return _func
