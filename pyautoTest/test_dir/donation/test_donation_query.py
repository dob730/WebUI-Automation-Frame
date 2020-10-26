import seldom
from seldom import Seldom
from poium import PageWait
from pyautoTest.page.DonationPage import DonationPage
import os
import re

file_path = os.path.dirname(os.path.abspath(__file__))


class DonationNormalTest(seldom.TestCase):
    """捐款查詢/快速捐款退款/快速捐款取消退款"""

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


    #快速捐款退款
    def test_refund(self):
        """
        A simple test
        """

        page = DonationPage(Seldom.driver)
        self.sleep(0.5)
        self.select(name="createmode", value="f")
        self.select(name="donation_status", value="p")
        self.click(xpath="//button[@class='btn btn-success']")
        PageWait(page.query_form)
        search_count = self.get_text(xpath="//form[@name='listform']/div/div/span")
        num = re.findall(r'\d+', search_count)
        if (int(num[0])>100):
            count = 100
        else:
            count = int(num[0])

        for i in range(1, count+1):
            PageWait(page.query_form)
            self.sleep(0.5)
            self.click(xpath="//tr[%d]/td[last()]/button" % (i))  #
            self.sleep(0.5)
            if (self.get_text(xpath="//div[@class='card'][2]/div/div/div/div/table/tbody/tr/td[1]") == '信用卡'):
                self.click(xpath="//button[@class='btn btn-info btn-rounded btnSee']")
                self.sleep(0.5)
                if (self.get_attribute(xpath="//button[@class='btn btn-danger']",
                                       attribute="id") == 'confirm_cancelrefund'):
                    Seldom.driver.back()
                elif (self.get_attribute(xpath="//button[@class='btn btn-danger']", attribute="id") == 'refund_btn'):
                    self.click(id_="refund_btn")
                    self.sleep(0.5)
                    self.click(id_="refund_submit_btn")
                    self.click(id_="refund_sure_btn")
                    self.assertAlertText("退款建立  成功!")
                    self.accept_alert()
                    break
                else:
                    Seldom.driver.back()

            else:
                Seldom.driver.back()

    # 快速捐款取消退款
    def test_refund_reversal(self):

        page = DonationPage(Seldom.driver)
        page.donation_query.click()
        self.sleep(0.5)
        self.select(name="createmode", value="f")
        self.select(name="donation_status", value="p")
        self.click(xpath="//button[@class='btn btn-success']")
        PageWait(page.query_form)
        search_count = self.get_text(xpath="//form[@name='listform']/div/div/span")
        num = re.findall(r'\d+', search_count)
        if (int(num[0])>100):
            count = 100
        else:
            count = int(num[0])
        for i in range(1, count+1):
            PageWait(page.query_form)
            self.sleep(0.5)
            self.click(xpath="//tr[%d]/td[last()]/button" % (i))
            self.sleep(0.5)
            if (self.get_text(xpath="//div[@class='card'][2]/div/div/div/div/table/tbody/tr/td[1]") == '信用卡'):
                self.click(xpath="//button[@class='btn btn-info btn-rounded btnSee']")
                self.sleep(0.5)
                if (self.get_attribute(xpath="//button[@class='btn btn-danger']", attribute="id") == 'confirm_cancelrefund'):
                    self.click(id_="confirm_cancelrefund")
                    self.sleep(0.5)
                    self.click(id_="cancelrefund_sure_btn")
                    self.assertAlertText("取消退款建立  成功!")
                    self.accept_alert()
                    break
                elif (self.get_attribute(xpath="//button[@class='btn btn-danger']", attribute="id") == 'refund_btn'):
                    Seldom.driver.back()
                else:
                    Seldom.driver.back()

            else:
                Seldom.driver.back()


if __name__ == '__main__':
    seldom.main()
