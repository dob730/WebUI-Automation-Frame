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

file_path = os.path.dirname(os.path.abspath(__file__))


class DonationProjectTest(seldom.TestCase):
    """捐款專案建立"""

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
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li[1]/a/i")
        cls.click(cls, xpath="//ul[@id='sidebarnav']/li[1]/ul/li/a")

    @classmethod
    def tearDownClass(cls):
        pass

    @data(excel_to_list(file_path + "\data.xlsx", sheet="donation_project", line=1))
    def test_case(self, approvednumber, projectname, content, p_date_st, p_date_ed, upper_time, lower_time):
        """
        A simple test
        """

        page = DonationPage(Seldom.driver)
        PageWait(page.donation_approvednumber)

        self.click(name="approvednumber")
        self.type(name="approvednumber", text=approvednumber)
        self.type(name="projectname", text=projectname)
        self.type(name="content", text=content)
        self.click(id_="p_date_st")
        self.execute_script("document.getElementById('p_date_st').removeAttribute('readonly')")
        self.type(id_="p_date_st", text=p_date_st)
        self.execute_script("document.getElementById('p_date_ed').removeAttribute('readonly')")
        self.type(id_="p_date_ed", text=p_date_ed)
        self.execute_script("document.getElementById('upper_time').removeAttribute('readonly')")
        self.type(id_="upper_time", text=upper_time)
        self.execute_script("document.getElementById('lower_time').removeAttribute('readonly')")
        self.type(id_="lower_time", text=lower_time)
        self.type(id_="project_pic", text=file_path + "\Sc.jpg")
        self.click(id_='surecreate_btn')
        PageWait(page.show_message)
        self.assertEqual(self.get_text(id_="show_message"), "專案建立 成功!")


if __name__ == '__main__':
    seldom.main()
