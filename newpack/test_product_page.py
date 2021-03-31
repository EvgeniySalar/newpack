import time

import pytest
from selenium.webdriver import ActionChains

from home_page import HomePage


class TestSiteFunc:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, chrome_drv):
        self.home_page = HomePage(chrome_drv)
        yield chrome_drv

    def test_click_on_the_button(self, chrome_drv):
        self.home_page.button_guests_elements().click()
        assert self.home_page.button_increase_elements.is_displayed(), \
            "Window is not displayed"
        btn_click = self.home_page.button_increase_elements
        actions = ActionChains(chrome_drv)
        actions.double_click(btn_click).perform()
        assert self.home_page.section_elements().is_displayed(), \
            "Button is not clicked"

    def test_click_on_the_selection_1(self):
        self.home_page.section_elements().click()
        assert self.home_page.section_elements().is_enabled()
        self.home_page.section_child_age_element().click()
        assert self.home_page.section_child_age_element().is_enabled()

    def test_click_on_the_selection_2(self, chrome_drv):
        self.home_page.section_elements_2().click()
        assert self.home_page.section_elements_2().is_enabled()
        self.home_page.section_child_age_element_2().click()
        assert self.home_page.section_child_age_element_2().is_enabled()
        self.home_page.empty_field().click()
        assert self.home_page.empty_field().is_enabled()
