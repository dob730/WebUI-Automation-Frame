"""
page object model
Using the poium Library
https://github.com/SeldomQA/poium
```
> pip install poum
```
"""
import seldom
from seldom import Seldom
from seldom import data
from poium import PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.RecBillingPage import RecBillingPage
import os
from seldom.testdata.conversion import excel_to_list

file_path = os.path.dirname(os.path.abspath(__file__))


class YouTest(seldom.TestCase):
    """繳費單管理批次建立"""

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
        menubar.recbill.click()
        menubar.recbill_batch_create.click()



    @classmethod
    def tearDownClass(cls):
        pass

    @data(excel_to_list(file_path + "\data.xlsx", sheet="recbill_batch_create", line=1))
    def test_case(self, recbillname, duedate_day, allowancedate_day, recbillinfo_name):
        page = RecBillingPage(Seldom.driver)
        PageWait(page.recbillname)
        self.click(id_="recbillname")  # 點擊繳費單名稱欄位
        self.type(id_="recbillname", text=recbillname)  # 繳費單名稱
        self.select(name="duedate_day", value=duedate_day)  # 繳費單有效天數
        self.select(name="allowancedate_day", value=allowancedate_day)  # 繳費單寬限天數
        self.type(id_="recbillinfo_name", text=recbillinfo_name)  # 繳費項目名稱
        self.click(id_="sendquery_btn")
        PageWait(page.query_form)
        self.click(xpath="//tbody[@id='results']/tr/td/div/label")  # 點首筆資料checkbox
        self.click(id_="create_btn")  # 點選送出
        PageWait(page.show_message)
        self.click(id_="surecreate_btn")  # 送出reconfirm
        self.sleep(0.5)
        self.assertEqual(self.get_text(id_="show_recbillname"), "成功!")
        self.click(id_="close_btn")


