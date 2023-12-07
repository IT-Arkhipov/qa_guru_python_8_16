"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import time

import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture()
def browser_config():
    browser.config.driver = webdriver.Chrome()
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


def test_github_desktop(browser_config):
    browser.open('https://github.com')
    time.sleep(1)


def test_github_mobile(browser_config):
    pass
