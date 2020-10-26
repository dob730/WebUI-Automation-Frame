from selenium.common.exceptions import NoSuchElementException

import seldom
from seldom import Seldom
from poium import PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.BillingPage import BillingPage
import os
from datetime import datetime, timedelta
import re

file_path = os.path.dirname(os.path.abspath(__file__))


class YouTest(seldom.TestCase):
    """繳費單查詢"""

    @classmethod
    def setUpClass(cls):
        page = ServicePage(Seldom.driver)
        menubar = BillingPage(Seldom.driver)
        page.get("https://sit.1177tech.com.tw/SSO/external/login.jsp")
        page.userid_input = "ad21@sharklasers.com"
        page.pwd_input = "Qqqq1111"
        page.validate_input = "1111"
        page.login_button.click()
        page.big_apple_button.click()
        page.services.click()
        PageWait(page.service)
        page.billing.click()
        menubar.bill_query.click()



    @classmethod
    def tearDownClass(cls):
        pass


    def check_exists_by_xpath(self, xpath):
        try:
            Seldom.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def test_cancel(self):

        menubar = BillingPage(Seldom.driver)
        menubar.bill_query.click()
        self.select(id_="bill_status", value="C")
        self.click(xpath="//button[@class='btn btn-success']")
        self.sleep(0.5)

        self.click(xpath="//tr/td[last()]/button")
        self.sleep(0.5)
        self.click(id_="do_cancelbill_btn")
        self.sleep(0.5)
        self.click(id_="cancelbill_sure_btn")
        self.sleep(0.5)
        self.assertEqual(self.get_text(id_="cancelbill_showmessage"), "取消帳單 成功!")
        self.click(id_="cancelbill_close_btn")


    def test_refund(self):
        page = BillingPage(Seldom.driver)
        page.bill_query.click()
        yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y/%m/%d')
        self.execute_script("document.getElementById('billtimeed').removeAttribute('readonly')")
        self.click(id_="billtimeed")
        self.type(id_="billtimeed", text=yesterday)
        self.select(id_="bill_status", value="S")
        self.click(xpath="//button[@class='btn btn-success']")

        self.sleep(0.5)
        search_count = self.get_text(xpath="//form[@name='listform']/div/div/span")
        num = re.findall(r'\d+', search_count)

        if (int(num[0])>100):
            count = 100
        else:
            count = int(num[0])
        for i in range(1, count+1):
            self.sleep(0.5)
            self.click(xpath="//tr[%d]/td[last()]/button" % (i))
            self.sleep(0.5)
            if (self.get_text(xpath="//div[@id='main-wrapper']/div/div/div[2]/div/div[3]/div/div/div/div/table/tbody/tr/td[4]") == '信用卡'):
                self.click(xpath="//button[@type='button']")
                if (self.check_exists_by_xpath("//button[@class='btn btn-danger']")):
                    if (self.get_attribute(xpath="//button[@class='btn btn-danger']", attribute="id") == 'confirm_cancelrefund'):  # 取消退款
                        Seldom.driver.back()
                    elif(self.get_attribute(xpath="//button[@class='btn btn-danger']", attribute="id") == 'refund_btn'):  # 退款
                        self.click(id_="refund_btn")
                        PageWait(page.dialog)
                        self.click(id_="refund_submit_btn")
                        self.click(id_="refund_sure_btn")
                        self.assertAlertText("退款建立  成功!")
                        self.accept_alert()
                        break

                else:    # 不存在退款按鍵
                    Seldom.driver.back()
            else:        # 非信用卡
                Seldom.driver.back()



    def test_refund_reversal(self):
        yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y/%m/%d')
        page = BillingPage(Seldom.driver)
        page.bill_query.click()
        self.execute_script("document.getElementById('billtimeed').removeAttribute('readonly')")
        self.click(id_="billtimeed")
        self.type(id_="billtimeed", text=yesterday)
        self.select(id_="bill_status", value="S")
        self.click(xpath="//button[@class='btn btn-success']")

        self.sleep(0.5)
        search_count = self.get_text(xpath="//form[@name='listform']/div/div/span")
        num = re.findall(r'\d+', search_count)

        if (int(num[0])>100):
            count = 100
        else:
            count = int(num[0])

        for i in range(1, count+1):
            self.sleep(0.5)
            self.click(xpath="//tr[%d]/td[last()]/button" % (i))
            self.sleep(0.5)

            if (self.get_text(xpath="//div[@id='main-wrapper']/div/div/div[2]/div/div[3]/div/div/div/div/table/tbody/tr/td[4]") == '信用卡'):
                self.click(xpath="//button[@type='button']")
                if (self.check_exists_by_xpath("//button[@class='btn btn-danger']")):
                    if (self.get_attribute(xpath="//button[@class='btn btn-danger']", attribute="id") == 'confirm_cancelrefund'):  # 取消退款
                        self.click(id_="confirm_cancelrefund")
                        PageWait(page.dialog)
                        self.click(id_="cancelrefund_sure_btn")
                        self.assertAlertText("取消退款建立  成功!")
                        self.accept_alert()
                        break
                    elif(self.get_attribute(xpath="//button[@class='btn btn-danger']", attribute="id") == 'refund_btn'):  # 退款
                        Seldom.driver.back()
                else:    # 不存在退款按鍵
                    Seldom.driver.back()
            else:        # 非信用卡
                Seldom.driver.back()
