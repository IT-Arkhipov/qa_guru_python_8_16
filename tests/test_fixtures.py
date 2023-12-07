"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import time

import pytest

from page.sign_in import sign_in
from selene import browser, be, have
from selenium import webdriver


@pytest.fixture(params=[(2560, 1440), (1920, 1080)])
def desktop_dimension(request):
    width, height = request.param
    browser.config.driver = webdriver.Chrome()
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=[(414, 896), (430, 932)])
def mobile_dimension(request):
    width, height = request.param
    browser.config.driver = webdriver.Chrome()
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.mark.usefixtures("desktop_dimension")
def test_github_desktop():
    browser.open('https://github.com')
    sign_in.desktop_sign_in()


@pytest.mark.usefixtures("mobile_dimension")
def test_github_mobile():
    browser.open('https://github.com')
    sign_in.mobile_sign_in()
