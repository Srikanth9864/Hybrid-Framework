from selenium import webdriver
from Library.config import Config
import pytest

driver = None

@pytest.fixture(autouse=True)
def _driver():
    global driver
    if Config.BROWSER_NAME.upper() == 'CHROME':
        driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH)
    elif Config.BROWSER_NAME.upper() == 'FIREFOX':
        driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH)
    else:
        driver = webdriver.Ie(Config.IE_DRIVER_PATH)
    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def _capture_screenshot():
    return driver.save_screenshot("report")


# code to attach screenshot to the html report generated
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasfail")
        # if report: # attaches screenshots for all steps
        if (report.skipped and report.fail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.image(_capture_screenshot()))
        report.extra = extra
  
# passing command line arguments to conftest.py
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser", action="store", default="chrome", help="browser type chrome/firefox/edge"
#     )

# @fixture
# def _driver(request):
#     browser_type = request.config.getoption("--browser")
#     if browser_type.lower() == 'chrome':
#         driver = webdriver.Chrome("./chromedriver")
#     elif browser_type.lower() == "firefox":
#         driver = webdriver.Chrome("./geckodriver")
#     elif browser_type.lower() == "edge":
#         driver = webdriver.Edge("./geckodriver")
#     elif browser_type.lower() == "safari":
#         driver = webdriver.Safari()
#     else:
#         raise NameError('Unknown Browser')
#     driver.get("http://demowebshop.tricentis.com/")
#     driver.maximize_window()
#     yield driver
#     driver.close()

@pytest.fixture(scope="class")
def init_chrome(request):
    driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH)
    driver.get(Config.URL)
    driver.maximize_window()
    # cls is the name of the class from where init fixture is being called
    request.cls.driver = driver
    yield
    driver.quit()

#
# @pytest.fixture(scope="class")
# def init_firefox(request):
#     driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH)
#     driver.get(Config.URL)
#     driver.maximize_window()
#     # cls is the name of the class from where init fixture is being called
#     request.cls.driver = driver
#     yield
#     driver.quit()
