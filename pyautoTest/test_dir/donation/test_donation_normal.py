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
from pyautoTest.page.DonationPage import DonationPage
import os
from seldom.testdata.conversion import excel_to_list
from datetime import datetime, timedelta

file_path = os.path.dirname(os.path.abspath(__file__))



class DonationNormalTest(seldom.TestCase):
    """定額捐款建立"""

    @classmethod
    def setUpClass(cls):
        page = DonationPage(Seldom.driver)
        cls.get(cls, "https://sit.1177tech.com.tw/SSO/external/login.jsp")
        cls.type(cls, id_="USERID", text="ad21@sharklasers.com")
        cls.type(cls, name="PWD", text="Qqqq1111")
        cls.type(cls, name="validatecode", text="1111")
        cls.click(cls, class_name="btn")
        cls.click(cls, xpath="(//button[@type='button'])[6]")
        cls.click(cls, class_name="dropdown-toggle")
        PageWait(page.donation)
        cls.click(cls, xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[last()]")
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li[3]/a/i")
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li[3]/ul/li/a")

    @classmethod
    def tearDownClass(cls):
        pass



    @data(excel_to_list(file_path + "\data.xlsx", sheet="donation_normal", line=1))
    def test_case(self, usename_input, donation_amount, date, name_1, num_1, sendmobile_1):
        """
        定額建立
        """
        tomorrow = datetime.strftime(datetime.now() + timedelta(1), '%Y/%m/%d')
        page = DonationPage(Seldom.driver)
        PageWait(page.usename_input)
        self.click(id_="usename_input")
        self.type(id_="usename_input", text=usename_input)
        self.type(id_="donation_amount", text=donation_amount)

        self.click(name="setdate")
        self.execute_script("document.getElementsByName('setdate')[0].removeAttribute('readonly')")

        self.type(name="setdate", text=tomorrow)
        self.click(xpath="//div[@class='col-md-12']/div/div/label")
        if (self.get_display(name="name_1")):
            self.type(name="name_1", text=name_1)
            self.type(name="num_1", text=num_1)
            self.type(name="sendmobile_1", text=sendmobile_1)

        self.click(id_='surecreate_btn')
        PageWait(page.show_message)
        self.assertEqual(self.get_text(id_="show_message"), "定額建立 成功")


if __name__ == '__main__':
    seldom.main()
