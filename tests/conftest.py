import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# .\.venv\Scripts\activate
# pytest --html=report.html
# key: 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
@pytest.fixture(scope="class")
def web_driver(request):

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # Close the browser
    driver.quit()
