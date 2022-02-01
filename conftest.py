import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help="Choose language: 'ru' or 'es' ")

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

    if browser_language == "es":
        print("\n ---- START BROWSER with lang='eng' ----")
        options.set_preference("intl.accept_languages",lang_parametrs['eng'])
    elif browser_language == 'ru':
        print("\n ---- START BROWSER with lang='rus' ----")
        options.set_preference("intl.accept_languages", lang_parametrs['rus'])
    else:
        raise pytest.UsageError("--browser_language should be 'ru' or 'es")
    browser = webdriver.Firefox(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()