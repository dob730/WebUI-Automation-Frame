import seldom
from seldom import Seldom
from seldom import data
from poium import PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.RecBillingPage import RecBillingPage
import os
from datetime import datetime, timedelta
import re
from selenium.common.exceptions import NoSuchElementException



file_path = os.path.dirname(os.path.abspath(__file__))


class YouTest(seldom.TestCase):
    """繳費單查詢、退款、取消退款、取消交易"""

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

    def check_exists_by_xpath(self, xpath):
        try:
            Seldom.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True


    def test_query(self):
        page = RecBillingPage(Seldom.driver)
        menubar = RecBillingPage(Seldom.driver)
        menubar.recbill.click()
        menubar.recbill_query.click()
        self.click(id_="sendquery_btn")
        PageWait(page.query_form)
        search_count = self.get_text(xpath="//form[@id='queryform2']/div/div/span")
        self.assertIn("[ 共 ", search_count)

    def test_cancel(self):
        page = RecBillingPage(Seldom.driver)
        self.select(name="status", value="c")
        self.click(id_="sendquery_btn")
        PageWait(page.query_form)
        PageWait(page.querydetail_btn)
        self.sleep(0.5)
        self.click(id_="querydetail_btn")
        self.sleep(0.5)
        self.click(id_="btn_disable")
        self.assertAlertText("成功!")
        self.accept_alert()

    def test_refund(self):
        yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y/%m/%d')
        page = RecBillingPage(Seldom.driver)
        menubar = RecBillingPage(Seldom.driver)
        menubar.recbill.click()
        menubar.recbill_query.click()
        self.execute_script("document.getElementById('timepaid_e').removeAttribute('readonly')")
        self.type(id_="timepaid_e", text=yesterday)
        self.click(xpath="//label[@class='custom-control custom-checkbox'][2]")
        self.click(xpath="//label[@class='custom-control custom-checkbox'][3]")
        self.click(id_="sendquery_btn")

        self.sleep(0.5)
        search_count = self.get_text(xpath="//form[@id='queryform2']/div/div/span")
        num = re.findall(r'\d+', search_count)
        if (int(num[0])>100):
            count = 100
        else:
            count = int(num[0])

        for i in range(1, count+1):
            self.sleep(0.5)
            self.click(xpath="//tr[%d]/td[last()]/button" % (i))
            self.sleep(0.5)
            self.click(xpath="//button[@id='paymentdata_btn']")
            self.sleep(0.5)
            if (self.check_exists_by_xpath("(//button[@class='btn btn-danger'])[1]") and self.check_exists_by_xpath("(//button[@class='btn btn-danger'])[2]")):  # 如果退款或取消退款同時存在，代表有按鍵可按
                if (self.get_text(xpath="(//button[@class='btn btn-danger'])[1]") == '退款'):
                    PageWait(page.boxSee)
                    self.click(id_="refund_btn")
                    PageWait(page.refund_submit)
                    self.click(id_="refund_submit_btn")
                    PageWait(page.refund_sure)
                    self.click(id_="refund_sure_btn")
                    self.assertAlertText("成功!")
                    self.accept_alert()
                    break
                else:
                    Seldom.driver.back()
            else:  # 如果沒有按鍵，回上一頁
                Seldom.driver.back()

    def test_refund_reversal(self):
        yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y/%m/%d')
        page = RecBillingPage(Seldom.driver)
        menubar = RecBillingPage(Seldom.driver)
        menubar.recbill.click()
        menubar.recbill_query.click()
        self.execute_script("document.getElementById('timepaid_e').removeAttribute('readonly')")
        self.click(id_="timepaid_e")
        self.type(id_="timepaid_e", text=yesterday)
        self.click(xpath="//label[@class='custom-control custom-checkbox'][2]")
        self.click(xpath="//label[@class='custom-control custom-checkbox'][3]")
        self.click(id_="sendquery_btn")


        self.sleep(0.5)
        search_count = self.get_text(xpath="//form[@id='queryform2']/div/div/span")
        num = re.findall(r'\d+', search_count)
        if (int(num[0])>100):
            count = 100
        else:
            count = int(num[0])

        for i in range(1, count+1):
            self.sleep(0.5)
            self.click(xpath="//tr[%d]/td[last()]/button" % (i))
            self.sleep(0.5)
            self.click(xpath="//button[@id='paymentdata_btn']")
            self.sleep(0.5)
            if (self.check_exists_by_xpath("(//button[@class='btn btn-danger'])[1]") and self.check_exists_by_xpath("(//button[@class='btn btn-danger'])[2]")):  # 如果退款或取消退款同時存在，代表有按鍵可按
                if(self.get_text(xpath="(//button[@class='btn btn-danger'])[2]") == '取消退款'):
                    self.click(xpath="(//button[@class='btn btn-danger'])[2]")
                    PageWait(page.cancelrefund)
                    self.click(id_="btn_cancelrefund")
                    self.assertAlertText("成功!")
                    self.accept_alert()
                    break
                else:
                    Seldom.driver.back()
            else:  # 如果沒有按鍵，回上一頁
                Seldom.driver.back()


