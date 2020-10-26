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
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.BillingPage import BillingPage
import os
from seldom.testdata.conversion import excel_to_list
import requests
import json

file_path = os.path.dirname(os.path.abspath(__file__))


class YouTest(seldom.TestCase):
    """定額捐款建立"""


    @classmethod
    def setUpClass(cls):
        page = ServicePage(Seldom.driver)
        cls.get(cls, "https://sit.1177tech.com.tw/SSO/external/login.jsp")
        cls.type(cls, id_="USERID", text="ad21@sharklasers.com")
        cls.type(cls, name="PWD", text="Qqqq1111")
        cls.type(cls, name="validatecode", text="1111")
        cls.click(cls, class_name="btn")
        cls.click(cls, xpath="(//button[@type='button'])[6]")
        cls.click(cls, class_name="dropdown-toggle")
        PageWait(page.service)
        cls.click(cls, xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[5]")
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li[1]/a/i")
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li[1]/ul/li/a")

    @classmethod
    def tearDownClass(cls):
        pass

    @data(excel_to_list(file_path + "\data.xlsx", sheet="create_fast", line=1))
    def test_case1(self, bill_name, receiver, email, mobile, total_amount, memo):
        """
        A simple test
        """

        page = BillingPage(Seldom.driver)

        self.click(name="bill_name")
        self.clear(name="bill_name")
        self.type(name="bill_name", text=bill_name)
        self.clear(name="name")
        self.type(name="name", text=receiver)
        if (email != ""):
            self.click(xpath="//div[@class='col-lg-6']/div[3]/label[2]")
            self.wait(2)
            self.clear(name="email")
            self.type(id_="email", text=email)
        if (mobile != ""):
            self.click(xpath="//div[@class='col-lg-6']/div[3]/label[3]")
            self.wait(2)
            self.clear(id_="mobile")
            self.type(id_="mobile", text=mobile)
        self.clear(id_="bill_totalamount")
        self.type(id_="bill_totalamount", text=total_amount)
        self.clear(name="billmemo")
        self.type(name="billmemo", text=memo)
        self.click(id_="surecreate_btn")
        PageWait(page.show_message)
        self.assertEqual(self.get_text(id_="show_message"), "快速建立帳單 成功!")
        self.click(id_="close_btn")
        self.refresh()

    def test_case2(self):
        self.sleep(0.5)
        page = BillingPage(Seldom.driver)
        page.bill_query.click()
        self.select(id_="bill_status", value="C")
        self.click(xpath="//button[@class='btn btn-success']")
        self.sleep(0.5)
        billnumber = self.get_text(xpath="//tr[1]/td[2]")

        data = {

            "action": "acceptpayment",
            "merchantnumber": "118460",
            "billnumber": billnumber,
            "paymenttype": "creditcard",
            "consumerip": "127.0.0.1",
            "1177payid": "789456456",
            "transmode": "N",
            "cardnumber": "4682358976116102",
            "cardexpiry": "202812",
            "cardcvc2": "057"

        }


        self.headers = {'content-type': 'application/json'}
        response = requests.post("https://sit.1177tech.com.tw/Billing/MobileConnectServlet", headers=self.headers,
                                 data=json.dumps(data))

        self.info = response.json()
        print(self.info)
        self.assertEqual(self.info["rc"], '0')

if __name__ == '__main__':
    seldom.main()
