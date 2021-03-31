from locators import MainPageLocators


class HomePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        # self.browser.implicitly_wait(timeout)

    def button_guests_elements(self):
        return self.driver.find_element_by_class_name(MainPageLocators.GUESTS_COUNT)

    @property
    def button_increase_elements(self):
        return self.driver.find_element_by_xpath(MainPageLocators.INCREASE_PERSON_NUMBER)

    def section_elements(self):
        return self.driver.find_element_by_xpath(MainPageLocators.CHILD_AGE_SELECTION)

    def section_child_age_element(self):
        return self.driver.find_element_by_xpath(MainPageLocators.DATA_GROUP_CHILD_AGE)

    def section_elements_2(self):
        return self.driver.find_element_by_xpath(MainPageLocators.DATA_GROUP_CHILD_AGE_2)

    def section_child_age_element_2(self):
        return self.driver.find_element_by_xpath(MainPageLocators.CHILD_AGE_SELECTION_1)

    def empty_field(self):
        return self.driver.find_element_by_xpath(MainPageLocators.EMPTY_FIELD)
