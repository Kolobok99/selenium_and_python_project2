import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='eng',
                     help="Choose language: 'rus' or 'eng' ")

@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption('--language')
    print(f"{browser_language=}")
    browser = None
    lang_parametrs = {
        'rus': "ru",
        'eng': "en-us",
    }
    options = Options()

    if browser_language == "eng":
        print("\n ---- START BROWSER with lang='eng' ----")
        options.set_preference("intl.accept_languages",lang_parametrs['eng'])
    elif browser_language == 'rus':
        print("\n ---- START BROWSER with lang='rus' ----")
        options.set_preference("intl.accept_languages", lang_parametrs['rus'])
    else:
        raise pytest.UsageError("--browser_language should be 'rus' or 'eng")
    browser = webdriver.Firefox(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()