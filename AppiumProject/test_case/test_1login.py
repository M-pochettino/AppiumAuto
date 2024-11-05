from AppiumProject.common.UnittestFunc import UnittestFunc
from AppiumProject.pageObject.loginPage import LoginPage


class TestLogin(UnittestFunc):

    def test_01normal_case(self):
        logn = LoginPage(self.driver)
        logn.loginView()

