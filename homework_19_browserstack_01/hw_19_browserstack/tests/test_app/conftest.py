import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os

from config import settings
from utils import attach
from utils.attach import attach_screenshot

DEFAULT_PLATFORM_NAME = "android"
DEFAULT_PLATFORM_VERSION = "9.0"
DEFAULT_DEVICE_NAME = "Google Pixel 3"


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        default="android",
        help="Platform to test: 'android' or 'ios'"
    )
    parser.addoption(
        "--device",
        default="Google Pixel 3",
        help="Override default device (e.g. 'iPhone 14 Pro Max', 'Google Pixel 3')"
    )
    parser.addoption(
        "--os-version",
        default="9.0",
        help="Version platform ('9.0' for android, '16' for ios)"
    )


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    platform = request.config.getoption("--platform")
    device = request.config.getoption("--device")
    version = request.config.getoption("--os-version")

    platform = platform if platform != "" else DEFAULT_PLATFORM_NAME
    device = device if device != "" else DEFAULT_DEVICE_NAME
    version = version if version != "" else DEFAULT_PLATFORM_VERSION

    options = UiAutomator2Options().load_capabilities({"""Это driver options"""
                                                       # Specify device and os_version for testing
                                                       "platformName": platform,
                                                       "platformVersion": version,
                                                       "deviceName": device,

                                                       # Set URL of the application under test
                                                       "app": "bs://sample.app",

                                                       # Set other BrowserStack capabilities
                                                       'bstack:options': {
                                                           "projectName": "First Python project",
                                                           "buildName": "browserstack-build-1",
                                                           "sessionName": "BStack first_test",

                                                           # Set your access credentials
                                                           # со страницы https://app-automate.browserstack.com/dashboard/v2/quick-start/get-started
                                                           "userName": settings.BROWSERSTACK_USERNAME,
                                                           "accessKey": settings.BROWSERSTACK_ACCESSKEY
                                                       }
                                                       })

    #передаем селениуму драйвер
    #browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))


    yield

    attach_screenshot(browser)
    browser.quit()


