from selenium.webdriver.common.by import By

class LinkedInLoginPageLocators(object):

    LOGIN_MAIL = (By.ID, 'session_key-login')
    LOGIN_PASSWORD = (By.ID, 'session_password-login')
    LOGIN_SUBMIT = (By.NAME, 'signin')

class LinkedInMainPageLocators(object):
    SEARCH_INPUT = (By.ID, 'main-search-box')
    SEARCH_BUTTON = (By.NAME, 'search')

class LinkedInSearchResultsPageLocators(object):
    SEARCH_PEOPLE_ONLY = (By.XPATH, '//*[@id="search-types"]/div/ul/li[2]/a')
    SECOND_LEVEL_CONNECTIONS = (By.XPATH, '//*[@id="facet-N"]/fieldset/div/ol/li[3]/div/label')