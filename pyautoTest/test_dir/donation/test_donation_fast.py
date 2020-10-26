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
from seldom.testdata.conversion import excel_to_list
from pyautoTest.page.DonationPage import DonationPage
from pyautoTest.page.ServicePage import ServicePage
import os
import requests
import json


class DonationTest(seldom.TestCase):
    """快速捐款建立"""

    @classmethod
    def setUpClass(cls):
        page = ServicePage(Seldom.driver)
        menubar = DonationPage(Seldom.driver)
        page.get("https://sit.1177tech.com.tw/SSO/external/login.jsp")
        page.userid_input = "ad21@sharklasers.com"
        page.pwd_input = "Qqqq1111"
        page.validate_input = "1111"
        page.login_button.click()
        page.big_apple_button.click()
        page.services.click()
        PageWait(page.donation)
        page.donation.click()
        menubar.donation_quick.click()

    @classmethod
    def tearDownClass(cls):
        pass

    file_path = os.path.dirname(os.path.abspath(__file__))

    @data(excel_to_list(file_path + "\data.xlsx", sheet="donation_fast", line=1))
    def test_case1(self, usename, amount, mobile):
        """
        A simple test
        """

        page = DonationPage(Seldom.driver)
        PageWait(page.usename_input)
        page.usename_input.click()
        page.usename_input.clear()
        page.usename_input.send_keys(usename)
        page.donation_amount.click()
        page.donation_amount.clear()
        page.donation_amount.send_keys(amount)
        page.mobile.clear()
        page.mobile.send_keys(mobile)
        page.select.select_by_value("5")
        page.send.click()
        PageWait(page.close_button)
        PageWait(page.show_message)
        self.assertEqual(page.show_message.text, "快速捐款發送完成!")
        page.close_button.click()

    # def test_case2(self):
    #     page = DonationPage(Seldom.driver)
    #     page.donation_query.click()
    #     self.sleep(0.5)
    #     self.select(name="donation_status", value="c")
    #     self.click(xpath="//button[@class='btn btn-success']")
    #     PageWait(page.query_form)
    #     # search_count = self.get_text(xpath="//form[@name='listform']/div/div/span")
    #     billnumber = self.get_text(xpath="//tr[1]/td[2]")
    #     data = {
    #
    #             "action": "acceptpayment",
    #             "merchantnumber": "118460",
    #             "billnumber": billnumber,
    #             "paymenttype": "creditcard",
    #             "transmode": "N",
    #             "cardnumber": "4682358976116102",
    #             "cardexpiry": "202812",
    #             "1177payid": "9527",
    #             "name": "王大明",
    #             "idnumber": "A123456789",
    #             "mobile": "0912345678",
    #             "email": "admin@1177tech.com.tw",
    #             "consumerip": "127.0.0.1",
    #             "receipttype": "year",
    #             "open_credittype": "e",
    #             "receipt_title": "壹壹柒柒科技股份有限公司",
    #             "receipt_taxid": "50751195",
    #             "receipt_address": "臺北市內湖區瑞光路268號11樓"
    #
    #             }
    #
    #
    #     self.headers = {'content-type': 'application/json'}
    #     response = requests.post("https://sit.1177tech.com.tw/Donation/MobileConnectServlet", headers=self.headers, data=json.dumps(data))
    #
    #     self.info = response.json()
    #     print(self.info)
    #     self.assertEqual(self.info["rc"], '0')
    # def test_case2(self):
    #     page = DonationPage(Seldom.driver)
    #     page.donation_query.click()
    #     self.sleep(0.5)
    #     self.select(name="donation_status", value="c")
    #     self.click(xpath="//button[@class='btn btn-success']")
    #     PageWait(page.query_form)
    #     # search_count = self.get_text(xpath="//form[@name='listform']/div/div/span")
    #     billnumber = self.get_text(xpath="//tr[1]/td[2]")
    #     data = {
    #
    #         "idnumber": "A123456789",
    #         "mobile": "0912111111",
    #         "consumerip": "211.72.15.174",
    #         "merchantnumber": "118460",
    #         "open_credittype": "d",
    #         "receipttype": "no",
    #         "billnumber": billnumber,
    #         "name": "王小明",
    #         "action": "acceptpayment",
    #         "paymenttype": "each",
    #         "email": "abc@1177tech.com.tw",
    #         "1177payid": "498269",
    #         "id": "Q120196476",
    #         "user_number": "0911222340",
    #         "bankid": "011",
    #         "bankaccount": "0063242000503054"
    #
    #     }
    #     print(data)
    #     self.headers = {'content-type': 'application/json'}
    #     response = requests.post("https://sit.1177tech.com.tw/Donation/MobileConnectServlet", headers=self.headers,
    #                              data=json.dumps(data))
    #
    #     self.info = response.json()
    #     print(self.info)
    #     self.assertEqual(self.info["rc"], '0')


if __name__ == '__main__':
    seldom.main(browser="chrome_headless", debug=True)
