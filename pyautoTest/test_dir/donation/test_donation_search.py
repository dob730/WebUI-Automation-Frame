import seldom
from seldom import Seldom
from poium import PageWait
from pyautoTest.page.DonationPage import DonationPage
import re

class DonationRegressionTest(seldom.TestCase):
    """捐款查詢回歸測試"""

    @classmethod
    def setUpClass(cls):
        page = DonationPage(Seldom.driver)
        page.get("https://sit.1177tech.com.tw/SSO/external/login.jsp")
        page.userid_input = "ad21@sharklasers.com"
        page.pwd_input = "Qqqq1111"
        page.validate_input = "1111"
        page.login_button.click()
        page.button.click()
        page.services.click()
        PageWait(page.donation)
        page.donation.click()
        page.donation_query.click()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_regression(self):
        """
        A simple test
        """

        page = DonationPage(Seldom.driver)
        self.sleep(0.5)
        # 點擊查詢鍵
        self.click(xpath="//button[@class='btn btn-success']")
        PageWait(page.query_form)
        search_count = self.get_text(xpath="//form[@name='listform']/div/div/span")
        num = re.findall(r'\d+', search_count)
        order_number_new = self.get_text(xpath="(//table[@class='table color-table muted-table']/tbody/tr/td[2])[1]")
        if (int(num[0])>100):
            self.sleep(0.5)
            self.click_text("2")
        order_number_old = self.get_text(xpath="(//table[@class='table color-table muted-table']/tbody/tr/td[2])[1]")
        self.assertNotEqual(order_number_new, order_number_old)
        self.sleep(0.5)
        
        # 查詢拉出少量資料
        self.type(id_="keyword", text="abc")
        # 點擊查詢鍵
        self.click(xpath="//button[@class='btn btn-success']")
        PageWait(page.query_form)
        search_count_by_keyword = self.get_text(xpath="//form[@name='listform']/div/div/span")
        num_by_keyword = re.findall(r'\d+', search_count_by_keyword)
        self.assertGreater(int(num_by_keyword[0]), 1)
        self.clear(id_="keyword")
        self.sleep(0.5)

        #指定某個訂單DO1184600000546
        self.type(id_="donationnumber", text="DO1184600000546")
        # 點擊查詢鍵
        self.click(xpath="//button[@class='btn btn-success']")
        PageWait(page.query_form)
        search_count_by_order = self.get_text(xpath="//form[@name='listform']/div/div/span")
        num_by_order = re.findall(r'\d+', search_count_by_order)
        self.assertEqual(int(num_by_order[0]), 1)
        self.clear(id_="donationnumber")


