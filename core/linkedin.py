from modules import *

class LinkedInCore(object):

    def __init__(self):
        self.config_path = os.path.join(os.getcwd(), 'core', 'credentials.ini')
        self.settings = {}
        self.config_parser(self.config_path)
        self.driver = None
        self.select_driver()
        self.wait = WebDriverWait(self.driver, 30)

    def config_parser(self, config_location):
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.config_path)
            for section in config.sections():
                for option in config.options(section):
                    self.settings[option] = config.get(section, option)
        except StandardError:
            raise

    def chrome(self):
        try:
            self.driver = webdriver.Chrome(executable_path=self.settings.get('chromedriver_location'))
            width = self.driver.execute_script('return window.screen.availWidth')
            height = self.driver.execute_script('return window.screen.availHeight')
            self.driver.set_window_position(0, 0)
            self.driver.set_window_size(width, height)
        except StandardError:
            raise

    def firefox(self):
        try:
            self.driver = webdriver.Firefox(executable_path=self.settings.get('geckodriver_location'))
            self.driver.maximize_window()
        except StandardError:
            raise

    def select_driver(self):
        try:
            if self.settings is not None:
                desired_browser = self.settings.get('selected_driver')
                if desired_browser == "chrome":
                    self.chrome()
                elif desired_browser == "firefox":
                    self.firefox()
                else:
                    print "Desired browser is not available.Please change it from credentials.ini file"
        except StandardError:
            raise

class LinkedInLoginPage(LinkedInCore):

    def login_with_account(self):
        try:
            if self.settings is not None:
                self.driver.get('https://www.linkedin.com/uas/login')
                user_mail = self.settings.get('user_mail')
                user_password = self.settings.get('user_password')
                self.wait.until(ec.element_to_be_clickable(LinkedInLoginPageLocators.LOGIN_MAIL)).send_keys(user_mail)
                self.wait.until(ec.element_to_be_clickable(LinkedInLoginPageLocators.LOGIN_PASSWORD))\
                    .send_keys(user_password)
                self.wait.until(ec.element_to_be_clickable(LinkedInLoginPageLocators.LOGIN_SUBMIT)).click()
                time.sleep(3)
        except StandardError:
            raise

class LinkedInMainPage(LinkedInCore):

    def search_for(self):
        try:
            if self.settings is not None:
                search_for = self.settings.get('search_for')
                self.wait.until(ec.element_to_be_clickable(LinkedInMainPageLocators.SEARCH_INPUT)).send_keys(search_for)
                self.wait.until(ec.element_to_be_clickable(LinkedInMainPageLocators.SEARCH_BUTTON)).click()
        except StandardError:
            raise

class LinkedInSearchResultPage(LinkedInCore):

    def filter_results(self):
        try:
            if self.settings is not None:
                self.wait.until(ec.element_to_be_clickable(LinkedInSearchResultsPageLocators.SEARCH_PEOPLE_ONLY))\
                    .click()
                time.sleep(3)
                self.wait.until(ec.element_to_be_clickable(LinkedInSearchResultsPageLocators.SECOND_LEVEL_CONNECTIONS))\
                    .click()
                time.sleep(3)
        except StandardError:
            raise

    def send_connect_request(self):
        try:
            if self.settings is not None:
                search_result = self.driver.find_element_by_xpath('//*[@id="results_count"]/div/p/strong[1]')
                search_result_count = int(search_result.get_attribute('textContent').replace(',',''))
                page_count = search_result_count/10
                base_url = self.driver.current_url
                for page in range(1, page_count+1):
                    new_url = base_url + '&page_num={0}'.format(page)
                    self.driver.get(new_url)
                    all_primary_buttons = self.driver.find_elements_by_class_name('primary-action-button')
                    for primary_button in all_primary_buttons:
                        primary_button.click()
                        time.sleep(2)
        except StandardError:
            raise







