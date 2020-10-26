import seldom
from seldom import Seldom
from poium import PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.AccountPage import AccountPage
import os

file_path = os.path.dirname(os.path.abspath(__file__))


class YouTest(seldom.TestCase):
    """繳費單查詢"""

    @classmethod
    def setUpClass(cls):
        page = ServicePage(Seldom.driver)
        menubar = AccountPage(Seldom.driver)
        page.get("https://sit.1177tech.com.tw/SSO/external/login.jsp")
        page.userid_input = "ad21@sharklasers.com"
        page.pwd_input = "Qqqq1111"
        page.validate_input = "1111"
        page.login_button.click()
        page.big_apple_button.click()
        page.services.click()
        PageWait(page.service)
        page.account.click()
        menubar.account_withdraw.click()
        menubar.withdraw.click()



    @classmethod
    def tearDownClass(cls):
        pass

    def test_case(self):
        page = AccountPage(Seldom.driver)
        self.type(id_="input_withdrawal_amount_cc", text="50")
        self.click(id_="button_confirm_withdrawal_amount_cc")
        PageWait(page.dialog1)
        self.click(xpath="//button[@class='btn btn-success']")
        self.assertAlertText("提領成功")
        self.accept_alert()

        self.type(id_="input_withdrawal_amount_ncc", text="50")
        self.click(id_="button_confirm_withdrawal_amount_ncc")
        PageWait(page.dialog2)
        self.click(xpath="(//button[@class='btn btn-success'])[2]")
        self.assertAlertText("提領成功")
        self.accept_alert()

    def test_withdraw_cancel(self):
        page = AccountPage(Seldom.driver)
        page.account_withdraw.click()
        page.withdraw_cancel.click()
        self.click(xpath="//button[@type='submit']")
        self.click(xpath="(//button[@type='button'])[2]")
        self.assertAlertText("取消提領成功")
        self.accept_alert()
