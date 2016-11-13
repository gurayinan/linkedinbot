from core.linkedin import *

class LinkedInTestClass(unittest.TestCase, LinkedInLoginPage, LinkedInMainPage, LinkedInSearchResultPage):

    def setUp(self):
        LinkedInLoginPage.__init__(self)

    def test_main(self):
        self.login_with_account()
        self.search_for()
        self.filter_results()
        self.send_connect_request()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()