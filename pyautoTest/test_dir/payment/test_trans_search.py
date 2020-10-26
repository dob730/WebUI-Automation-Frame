import seldom
from seldom import Seldom
from poium import PageWait
from pyautoTest.page.PaymentPage import PaymentPage
import re
from pyautoTest.common import Common

class PaymentRegressionTest(seldom.TestCase):
    """線上收款回歸測試"""

    @classmethod
    def setUpClass(cls):
        page = PaymentPage(Seldom.driver)
        page.get("https://sit.1177tech.com.tw/SSO/external/login.jsp")
        page.userid_input = "ad21@sharklasers.com"
        page.pwd_input = "Qqqq1111"
        page.validate_input = "1111"
        page.login_button.click()
        page.button.click()
        page.services.click()
        PageWait(page.payment_service)
        page.payment_service.click()
        page.trans_manage.click()
        page.trans_query.click()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_regression(self):
        page = PaymentPage(Seldom.driver)
        # 點擊查詢鍵
        self.click(xpath="//button[@class='btn btn-success']")
        PageWait(page.query_form)
        search_count = self.get_text(xpath="//form[@name='form_orders_list']/div/div")
        num = re.findall(r'\d+', search_count)
        order_number_new = self.get_text(xpath="(//table[@class='table color-table muted-table']/tbody/tr/td[2])[1]")
        # 當前搜尋的筆數大於100筆就換頁
        if (int(num[0])>100):
            self.click_text("2")
        order_number_old = self.get_text(xpath="(//table[@class='table color-table muted-table']/tbody/tr/td[2])[1]")
        self.assertNotEqual(order_number_new, order_number_old)

        # 查詢拉出少量資料
        yesterday = Common.get_day("%Y/%m/%d", -1)
        self.execute_script("document.getElementById('timecreated_s').removeAttribute('readonly')")
        self.type(id_="timecreated_s", text=yesterday)
        self.execute_script("document.getElementById('timecreated_e').removeAttribute('readonly')")
        self.type(id_="timecreated_e", text=yesterday)
        # 點擊查詢鍵
        self.click(xpath="//button[@class='btn btn-success']")
        PageWait(page.query_form)
        search_count_by_date = self.get_text(xpath="//form[@name='form_orders_list']/div/div")
        num_by_date = re.findall(r'\d+', search_count_by_date)
        self.assertGreater(int(num_by_date[0]), 1)
        self.click(xpath="//button[@class='btn btn-inverse']")

        #指定某個訂單20200811134656
        self.type(id_="firstName", text="20200811134656")
        # 點擊查詢鍵
        self.click(xpath="//button[@class='btn btn-success']")
        PageWait(page.query_form)
        search_count_by_order = self.get_text(xpath="//form[@name='form_orders_list']/div/div")
        num_by_order = re.findall(r'\d+', search_count_by_order)
        self.assertEqual(int(num_by_order[0]), 1)
        # 清除
        self.click(xpath="//button[@class='btn btn-inverse']")
