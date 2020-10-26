"""
page object model
Using the poium Library
https://github.com/SeldomQA/poium
```
> pip install poum
```
"""

import seldom
from seldom import Seldom, excel_to_list, data
from poium import PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.BillingPage import BillingPage
import os

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
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li[2]/a/i")
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li[2]/ul/li/a")

    @classmethod
    def tearDownClass(cls):
        pass

    @data(excel_to_list(file_path + "\data.xlsx", sheet="create_paylink", line=1))
    def test_case(self, paylink_name, min_qty, max_qty, valid_day, product_name1, product_name2, product_name3,
                  product_name4, product_name5, product_amount1, product_amount2, product_amount3, product_amount4,
                  product_amount5, qty1, qty2, qty3, qty4, qty5):
        """
        A simple test
        """

        name_list = [product_name1, product_name2, product_name3, product_name4, product_name5]
        amount_list = [product_amount1, product_amount2, product_amount3, product_amount4, product_amount5]
        qty_list = [qty1, qty2, qty3, qty4, qty5]

        page = BillingPage(Seldom.driver)
        self.click(name="paylinkname")
        self.type(name="paylinkname", text=paylink_name)
        self.clear(id_="min_qty")
        self.type(id_="min_qty", text=min_qty)
        self.clear(id_="max_qty")
        self.type(id_="max_qty", text=max_qty)
        self.type(name="valid_day", text=valid_day)
        for i in range(5):
            if (name_list[i] != ""):
                self.type(id_="a_productname_input", text=name_list[i])
                self.type(id_="productamount", text=amount_list[i])
                self.type(id_="qty", text=qty_list[i])
                self.click(id_="btn")
        self.click(id_="surecreate_btn")
        PageWait(page.show_message)
        self.click(id_="close_btn")
        PageWait(page.copylink)
        copylink = self.get_text(xpath="//div[@id='copylink']")
        self.get(copylink)
        self.type(id_="name", text="fdasfda")
        self.type(id_="email", text="aaa@bbb.com")
        self.type(id_="tel", text="0912111111")
        self.type(id_="remark", text="備註")
        self.click(class_name="btn")
        self.sleep(0.5)
        self.type(name="cc1", text="4682")
        self.type(name="cc2", text="3589")
        self.type(name="cc3", text="7611")
        self.type(name="cc4", text="6102")
        self.type(name="expiry_mm", text="03")
        self.type(name="expiry_yy", text="30")
        self.type(name="csc_cvv", text="057")
        self.type(name="cc_email", text="aba@ddd.com")
        self.type(id_="validatecode", text="1111")
        self.click(id_="cc_sendbtn")


if __name__ == '__main__':
    seldom.main()
