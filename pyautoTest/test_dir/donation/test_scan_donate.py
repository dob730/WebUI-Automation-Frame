import seldom
from seldom import Seldom
from seldom import data
from poium import PageWait
from seldom.testdata.conversion import excel_to_list
from pyautoTest.page.DonationPage import DonationPage
from pyautoTest.page.ServicePage import ServicePage
import os


class DonationTest(seldom.TestCase):
    """快速捐款建立"""

    # @classmethod
    # def setUpClass(cls):
    #
    #
    # @classmethod
    # def tearDownClass(cls):
    #     pass

    file_path = os.path.dirname(os.path.abspath(__file__))

    @data(excel_to_list(file_path + "\data.xlsx", sheet="scan_donate", line=1))
    def test_case1(self, amount, name, payphone, email, cardnumber, cardexpiry, cardcvc, validatecode):
        """
        A simple test
        """
        page = ServicePage(Seldom.driver)
        page.get("https://sit.1177pay.com.tw/Donation/scancameradonation/ScanDonate.jsp?key=4e230f4073114180")
        self.sleep(1)
        page = DonationPage(Seldom.driver)  # 拿driver
        page.amount.send_keys(amount)
        page.next_button.click()
        self.sleep(1)
        self.sleep(0.5)
        # page2
        page.name.send_keys(name)
        self.sleep(0.5)
        page.payphone.send_keys(payphone)
        self.sleep(0.5)
        page.email.send_keys(email)
        self.sleep(0.5)
        page.next_button.click()
        self.sleep(1)
        page.cardnumber.send_keys(cardnumber)
        self.sleep(0.5)
        print(cardexpiry)
        # page.cardexpiry.send_keys(cardexpiry)
        self.sleep(0.5)
        page.cardcvc.send_keys(cardcvc)
        self.sleep(0.5)
        page.validatecode.send_keys(validatecode)
        self.sleep(0.5)
        # page.confirm_pay.click()

        self.assertEqual(page.trans_result.text, "捐款成功！")

