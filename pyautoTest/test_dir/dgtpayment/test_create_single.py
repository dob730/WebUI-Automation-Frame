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
from pyautoTest.page.DgtPaymentPage import DgtPaymentPage
import os
from seldom.testdata.conversion import excel_to_list

file_path = os.path.dirname(os.path.abspath(__file__))



class YouTest(seldom.TestCase):
    """商品單筆建立"""

    @classmethod
    def setUpClass(cls):
        page = DgtPaymentPage(Seldom.driver)
        cls.get(cls, "https://sit.1177tech.com.tw/SSO/external/login.jsp")
        cls.type(cls, id_="USERID", text="ad21@sharklasers.com")
        cls.type(cls, name="PWD", text="Qqqq1111")
        cls.type(cls, name="validatecode", text="1111")
        cls.click(cls, class_name="btn")
        cls.click(cls, xpath="(//button[@type='button'])[6]")
        cls.click(cls, class_name="dropdown-toggle")
        PageWait(page.dgtPayment)
        cls.click(cls, xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[last()-1]")
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li/a/i")
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li/ul/li/a")

    @classmethod
    def tearDownClass(cls):
        pass



    @data(excel_to_list(file_path + "\data.xlsx", sheet="create_single", line=1))
    def test_case(self, product_name, product_amount, mobile):
        """
        A simple test
        """

        page = DgtPaymentPage(Seldom.driver)
        PageWait(page.product_name)
        self.click(name="productname")
        self.type(name="productname", text=product_name)
        self.click(name="productamount")
        self.type(id_="productamount", text=product_amount)
        self.click(xpath="//div[@class='form-group mb-3 pl-0']/div/label[1]")
        self.wait(2)
        self.click(name="mobile_app")
        self.type(name="mobile_app", text=mobile)
        self.click(xpath="//button[@type='button']")
        self.assertAlertText("單筆建立  成功!")
        self.accept_alert()



if __name__ == '__main__':
    seldom.main()
