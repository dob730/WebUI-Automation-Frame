import seldom
from seldom import Seldom
from seldom import data
from poium import PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.RecBillingPage import RecBillingPage
import os
from seldom.testdata.conversion import excel_to_list
import datetime

file_path = os.path.dirname(os.path.abspath(__file__))


class YouTest(seldom.TestCase):
    """繳費收款預約建立"""

    @classmethod
    def setUpClass(cls):
        page = ServicePage(Seldom.driver)
        menubar = RecBillingPage(Seldom.driver)
        page.get("https://sit.1177tech.com.tw/SSO/external/login.jsp")
        page.userid_input = "ad21@sharklasers.com"
        page.pwd_input = "Qqqq1111"
        page.validate_input = "1111"
        page.login_button.click()
        page.big_apple_button.click()
        page.services.click()
        PageWait(page.service)
        page.recbilling.click()
        menubar.reservation.click()
        menubar.recurrence_create.click()

    @classmethod
    def tearDownClass(cls):
        pass

    def get_time(self):
        today = datetime.date.today()
        tommorrow = today + datetime.timedelta(days=1)
        tommorrow.strftime("%Y/%m/%d")
        return tommorrow

    @data(excel_to_list(file_path + "\data.xlsx", sheet="recurrence_create", line=1))
    def test_case(self, recbillname, duedate_day, allowancedate_day, recurrence_date, recurrence_m_date, repeat):
        """0:recurrence_date 指定預約日期
        1:recurrence_m_date 預約固定月的日期
        2:repeat 重複幾次
        """
        if (recurrence_date != ""):
            recurrence_date = self.get_time()
        page = RecBillingPage(Seldom.driver)
        PageWait(page.recbillname)
        self.click(name="recbillname")
        self.type(name="recbillname", text=recbillname)  # 繳費單名稱
        self.select(name="duedate_day", value=duedate_day)  # 繳費單有效天數
        self.select(name="allowancedate_day", value=allowancedate_day)  # 繳費單寬限天數

        result = {}
        send_date_rule = [recurrence_date, recurrence_m_date, repeat]
        for cid, date_or_repeat in enumerate(send_date_rule):
            # 指定序號給result list，如果出現過的就依序把date_or_repeat塞進去
            result[cid] = date_or_repeat
        for key, value in result.items():
            if value != "":
                if key == 0:  # 指定發送日期
                    self.execute_script("document.getElementById('recurrence_s_date').removeAttribute('readonly')")
                    self.sleep(0.5)
                    recurrence_date = recurrence_date.__str__().format(timestamp=recurrence_date)
                    self.type(id_="recurrence_s_date", text=recurrence_date)

                elif key == 1:  # 設定預約周期
                    self.click(xpath="//div[@class='form-group mb-3 pl-0 d-flex']/div/label")
                    # 設定固定周期發送日期
                    self.select(id_="recurrence_m_date", value=recurrence_m_date)
                elif key == 2:  # 重複發送次數
                    self.click(xpath="//div[@class='form-group mb-3 pl-0 d-flex']/div[2]/label[1]")
                    self.select(id_="recurrence_totalcount", value=repeat)

        self.type(id_="recbillinfo_name", text="大樓")
        self.click(id_="sendquery_btn")
        PageWait(page.query_form)
        self.click(xpath="//tbody[@id='results']/tr/td/div/label")  # 點首筆資料checkbox
        self.click(id_="btn_create")  # 點選送出
        self.sleep(0.5)
        self.assertEqual(self.get_alert_text, "成功!")
        self.accept_alert()
