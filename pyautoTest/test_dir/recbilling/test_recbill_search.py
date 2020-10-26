import seldom
from seldom import Seldom
from poium import PageWait
from pyautoTest.page.RecBillingPage import RecBillingPage
from pyautoTest.page.ServicePage import ServicePage
import re
from pyautoTest.common import Common

class RecBillingRegressionTest(seldom.TestCase):
    """繳費收款回歸測試"""

    @classmethod
    def setUpClass(cls):
        page = RecBillingPage(Seldom.driver)
        service = ServicePage(Seldom.driver)
        service.get("https://sit.1177tech.com.tw/SSO/external/login.jsp")
        service.userid_input = "ad21@sharklasers.com"
        service.pwd_input = "Qqqq1111"
        service.validate_input = "1111"
        service.login_button.click()
        service.big_apple_button.click()
        service.services.click()
        PageWait(service.service)
        service.recbilling.click()
        page.recbill.click()
        page.recbill_query.click()



    @classmethod
    def tearDownClass(cls):
        pass

    def test_regression(self):
        page = RecBillingPage(Seldom.driver)
        # 點擊查詢鍵
        self.click(id_="sendquery_btn")
        PageWait(page.query_form)
        search_count = self.get_text(xpath="//form[@id='queryform2']/div/div/span")
        num = re.findall(r'\d+', search_count)
        order_number_new = self.get_text(xpath="(//table[@class='table color-table muted-table']/tbody/tr/td[2])[1]")
        # 當前搜尋的筆數大於100筆就換頁
        if (int(num[0])>100):
            self.click_text("2")
            order_number_old = self.get_text(xpath="(//table[@class='table color-table muted-table']/tbody/tr/td[2])[1]")
            self.assertNotEqual(order_number_new, order_number_old)

        # 查詢拉出少量資料
        self.click(id_="clearpara_btn")
        last_mouth = Common.get_day("%Y/%m/%d", -30)
        today = Common.get_day("%Y/%m/%d", 0)
        self.execute_script("document.getElementById('timecreated_s').removeAttribute('readonly')")
        self.type(id_="timecreated_s", text=last_mouth)
        self.execute_script("document.getElementById('timecreated_e').removeAttribute('readonly')")
        self.type(id_="timecreated_e", text=today)
        # 點擊查詢鍵
        self.click(id_="sendquery_btn")
        PageWait(page.query_form)
        search_count_by_date = self.get_text(xpath="//form[@id='queryform2']/div/div/span")
        num_by_date = re.findall(r'\d+', search_count_by_date)
        self.assertGreater(int(num_by_date[0]), 1)

        #指定某個訂單recbill_18671
        self.click(id_="clearpara_btn")
        self.type(name="keyword", text="recbill_18671")
        # 點擊查詢鍵
        self.click(id_="sendquery_btn")
        PageWait(page.query_form)
        search_count_by_order = self.get_text(xpath="//form[@id='queryform2']/div/div/span")
        num_by_order = re.findall(r'\d+', search_count_by_order)
        self.assertEqual(int(num_by_order[0]), 1)
        # 清除
        self.click(xpath="//button[@class='btn btn-inverse']")
