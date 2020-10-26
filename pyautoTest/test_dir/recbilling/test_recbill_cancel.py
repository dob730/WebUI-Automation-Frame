import seldom
from seldom import Seldom
from poium import PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.RecBillingPage import RecBillingPage
import os



file_path = os.path.dirname(os.path.abspath(__file__))


class YouTest(seldom.TestCase):
    """繳費單取消"""

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
        menubar.recbill_query.click()



    @classmethod
    def tearDownClass(cls):
        pass

    def test_cancel(self):
        page = RecBillingPage(Seldom.driver)
        self.select(id_="status", value="c")
        self.click(id_="sendquery_btn")
        element = Seldom.driver.find_element_by_xpath("//tr[1]/td[last()]/button")
        Seldom.driver.execute_script("arguments[0].click();", element)  # click檢視
        self.sleep(0.5)
        self.click(id_="btn_disable")
        self.assertAlertText("成功!")
        self.accept_alert()