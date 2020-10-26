import seldom
from seldom import Seldom
from poium import PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.RecBillingPage import RecBillingPage
import os

file_path = os.path.dirname(os.path.abspath(__file__))


class YouTest(seldom.TestCase):
    """繳費項目管理"""

    @classmethod
    def setUpClass(cls):
        page = ServicePage(Seldom.driver)
        menubar = RecBillingPage(Seldom.driver)
        page.get("https://sit.1177tech.com.tw/SSO/external/login.jsp")
        page.userid_input = "ad21@sharklasers.com"
        page.pwd_input = "Qqqq1111"
        page.validate_input = "1111"
        page.login_button.click()
        page.big_apple_button.click()
        page.services.click()
        PageWait(page.service)
        page.recbilling.click()
        menubar.recbill_info.click()
        menubar.recbill_info_query.click()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_query(self):
        page = RecBillingPage(Seldom.driver)
        menubar = RecBillingPage(Seldom.driver)
        menubar.recbill_info.click()
        menubar.recbill_info_query.click()
        self.click(id_="cellphone")
        self.type(id_="cellphone", text="0912111111")
        self.click(id_="sendquery_btn")
        PageWait(page.query_form)
        search_count = self.get_text(xpath="//form[@id='queryform2']/div/div/span")
        self.assertIn("[ 共 ", search_count)

    def test_delete(self):
        page = RecBillingPage(Seldom.driver)
        PageWait(page.recbillinfo_name)
        self.click(id_="cellphone")
        self.type(id_="cellphone", text="0912111111")
        self.click(id_="sendquery_btn")
        PageWait(page.query_form)
        self.sleep(0.5)
        self.click(xpath="//tr[1]/td/div/label")
        # PageWait(page.view_deletemessage)
        self.sleep(0.5)
        self.click(id_="btn_recbillinfoList_delete")
        self.sleep(0.5)
        self.click(id_="btn_dodeleteListMsg")
        self.sleep(0.5)
        self.assertEqual(self.get_text(id_="view_deleteListMsg"), "成功!")
        self.sleep(0.5)
        self.click(id_="btn_closedeleteListMsg")

