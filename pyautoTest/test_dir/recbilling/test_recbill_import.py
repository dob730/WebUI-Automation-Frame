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
from poium import Page, PageElement, PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.RecBillingPage import RecBillingPage
import os
from seldom.testdata.conversion import excel_to_list

file_path = os.path.dirname(os.path.abspath(__file__))


class YouTest(seldom.TestCase):
    """繳費單管理匯入建立"""

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
        menubar.recbill_import.click()

    @classmethod
    def tearDownClass(cls):
        pass

    @data(excel_to_list(file_path + "\data.xlsx", sheet="recbill_import", line=1))
    def test_case(self, recbillname, duedate_day, allowancedate_day):
        page = RecBillingPage(Seldom.driver)
        PageWait(page.recbillname)
        self.click(id_="recbillname")  # 點擊繳費單名稱欄位
        self.type(id_="recbillname", text=recbillname)  # 繳費單名稱
        self.select(name="duedate_day", value=duedate_day)  # 繳費單有效天數
        self.select(name="allowancedate_day", value=allowancedate_day)  # 繳費單寬限天數
        self.type(id_="recbillinfofile", text=file_path + "/recbillinfotemp.xlsx")  # 選擇檔案
        self.click(id_="btn_import")  # 確定匯入鍵
        PageWait(page.alert_success)
        self.assertEqual(self.get_text(xpath="//div[@id='success']/h3"), "繳費項目匯入成功!")
        self.click(xpath="//div[@class='modal-content']/div[3]/div/button")  # 確定匯入成功
        self.click(id_="create_btn")  # 發送form
        PageWait(page.surecreate_btn)
        self.click(id_="surecreate_btn")  # 確定發送按鍵
        self.click(id_="close_btn")  # 確定發送按鍵
