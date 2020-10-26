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
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li[1]/a/i")
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li[1]/ul/li[2]/a")

    @classmethod
    def tearDownClass(cls):
        pass

    @data(excel_to_list(file_path + "\data.xlsx", sheet="create_general", line=1))
    def test_case(self, bill_name, product_name1, product_name2, product_name3, product_name4, product_name5,
                  product_amount1,product_amount2, product_amount3, product_amount4, product_amount5, qty1, qty2, qty3, qty4, qty5,
                  receiver, email, mobile, memo):
        """
        A simple test
        """
        name_list = [product_name1, product_name2, product_name3, product_name4, product_name5]
        amount_list = [product_amount1, product_amount2, product_amount3, product_amount4, product_amount5]
        qty_list = [qty1, qty2, qty3, qty4, qty5]

        page = ServicePage(Seldom.driver)
        # PageWait(page.product_name)
        self.click(name="bill_name")
        self.type(name="bill_name", text=bill_name)
        for i in range(5):
            if (name_list[i] != ""):
                self.type(id_="a_productname_input", text=name_list[i])
                self.type(id_="productamount", text=amount_list[i])
                self.type(id_="qty", text=qty_list[i])
                self.click(id_="addbtn")
        if (email !=""):
            self.click(id_="send_df_mail")
            self.type(id_="email", text=email)
        if (mobile != ""):
            self.click(id_="send_df_app")
            self.type(id_="mobile", text=mobile)
        self.type(name="name", text=receiver)
        self.type(name="billmemo", text=memo)
        self.click(id_="surecreate_btn")
        PageWait(page.show_message)
        self.assertEqual(self.get_text(id_="show_message"), "一般建立帳單 成功!")
        self.click(id_="close_btn")


if __name__ == '__main__':
    seldom.main()
