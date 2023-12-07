"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser
from selenium import webdriver

from page.sign_in import sign_in


@pytest.fixture(params=[(2560, 1440), (1920, 1080), (414, 896), (430, 932)])
def browser_config(request):
    width, height = request.param
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser.config.driver = webdriver.Chrome(options=options)
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.mark.parametrize('browser_config', [(2560, 1440), (1920, 1080)], indirect=True)
def test_github_desktop(browser_config):
    browser.open('https://github.com')
    sign_in.desktop_sign_in()


@pytest.mark.parametrize('browser_config', [(414, 896), (430, 932)], indirect=True)
def test_github_mobile(browser_config):
    browser.open('https://github.com')
    sign_in.mobile_sign_in()

