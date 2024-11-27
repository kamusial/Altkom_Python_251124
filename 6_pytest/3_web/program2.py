from selenium import webdriver
from POM import LoginPage
from program_demo import make_screenshot
from selenium.webdriver.common.by import By
from time import sleep
import pytest

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
    ]

@pytest.mark.skip(reason='not implemented')
@pytest.mark.parametrize('user, passwd, url', test_data)
def test_login_page(user, passwd, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.print_page_info()
    page.enter_username(user)
    page.enter_password(passwd)
    page.click_login()
    sleep(1)
    page.print_page_info()
    try:
        assert page.get_current_url() == url, make_screenshot(driver)
    except AssertionError:
        print('Assercja nie przeszła')
        raise
    else:
        print('assercja przeszła')
    finally:
        print('Po asercji')
        driver.quit()

def test2():
    assert 2 == 2

def test3():
    assert 3 == 3
