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
    """繳費項目建立"""

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
        menubar.recbill_info_create.click()

    @classmethod
    def tearDownClass(cls):
        pass


    @data(excel_to_list(file_path + "\data.xlsx", sheet="recbillinginfo_create", line=1))
    def test_case(self, recbillinfo_name, recbillinfo_verify, amount, payername, cellphone_1, cellphone_2, cellphone_3, memo):
        phone_list = [cellphone_1, cellphone_2, cellphone_3]
        # 繳費項目
        self.click(name="recbillinfo_name")
        self.type(name="recbillinfo_name", text=recbillinfo_name)
        self.type(name="recbillinfo_verify", text=recbillinfo_verify)
        self.type(name="amount", text=amount)
        self.type(name="payername", text=payername)

        # 手機號碼
        self.type(name="cellphone_1", text=cellphone_1)
        for i in range(1, 3):
            if (phone_list[i]!=""):
                self.click(id_="addBtn2")
                self.type(name="cellphone_"+str(i+1)+"", text=phone_list[i])

        self.type(name="memo", text=memo)
        self.click(id_="btn_create")
        self.sleep(0.5)
        self.assertAlertText("成功!")
        self.accept_alert()


