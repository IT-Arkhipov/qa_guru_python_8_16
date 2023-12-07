"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import time

import pytest
from selene import browser
from selenium import webdriver

from page.sign_in import sign_in


@pytest.fixture(params=[(2560, 1440), (1920, 1080), (414, 896), (430, 932)],
                ids=['2560, 1440', '1920, 1080', '414, 896', '430, 932'])
def browser_config(request):
    width, height = request.param
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser.config.driver = webdriver.Chrome(options=options)
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture()
def is_desktop(browser_config):
    if (browser.config.window_width, browser.config.window_height) in ((2560, 1440), (1920, 1080)):
        return True
    else:
        return False


def test_github_desktop(is_desktop):
    if not is_desktop:
        pytest.skip('Not a desktop window resolution')
    browser.open('https://github.com')
    sign_in.desktop_sign_in()


def test_github_mobile(is_desktop):
    if is_desktop:
        pytest.skip('Not a mobile window resolution')
    browser.open('https://github.com')
    sign_in.mobile_sign_in()
