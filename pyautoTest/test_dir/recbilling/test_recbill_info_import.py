"""
page object model
Using the poium Library
https://github.com/SeldomQA/poium
```
> pip install poum
```
"""

import seldom
from seldom import Seldom, excel_to_list, data
from poium import PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.RecBillingPage import RecBillingPage
import os

file_path = os.path.dirname(os.path.abspath(__file__))


class YouTest(seldom.TestCase):
    """繳費項目匯入"""

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
        menubar.recbill_info_import.click()


    @classmethod
    def tearDownClass(cls):
        pass

    def test_case(self):
        page = RecBillingPage(Seldom.driver)
        self.type(id_="recbillinfofile", text=file_path + "/recbillinfotemp.xlsx")
        self.click(id_="btn_import")
        PageWait(page.alert_success)
        self.assertEqual(self.get_text(xpath="//div[@id='success']/h3"), "繳費項目匯入成功!")
        self.click(xpath="//div[@class='modal-content']/div[3]/div/button")  # 確定匯入成功