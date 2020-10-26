import seldom
from seldom import Seldom
from poium import PageWait
from pyautoTest.page.ServicePage import ServicePage
from pyautoTest.page.ECPage import ECPage




class YouTest(seldom.TestCase):
    """電商_查詢取消、退款、取消退款"""

    @classmethod
    def setUpClass(cls):
        page = ServicePage(Seldom.driver)
        page.get("https://sit.1177tech.com.tw/SSO/external/login.jsp")
        page.userid_input = "ad21@sharklasers.com"
        page.pwd_input = "Qqqq1111"
        page.validate_input = "1111"
        page.login_button.click()
        page.yen_store.click()
        page.services.click()
        PageWait(page.service)
        page.ec.click()




    @classmethod
    def tearDownClass(cls):
        pass

    def test_refund(self):
        # ElementNotInteractableException: Message: element not interactable

        ## 鼠标悬停
        # def hover(self,by,value):
        #     element = self.findElement(by,value)
        #     ActionChains(self.driver).move_to_element(element).perform()

        page = ECPage(Seldom.driver)
        # menu
        page.refund_manage.click()
        page.refund.click()
        # 查詢頁面
        PageWait(page.query_button)
        self.click(id_="query_btn")
        # self.click(xpath="//div[@id='main-wrapper']/div/div/div[3]/div/div/div/form/div[2]/div/div/table/tbody/tr/td")
        self.sleep(0.5)
        # PageWait(page.query_body)
        self.click(xpath="(//button[@type='button'])[3]") # 按檢視進入內容頁
        self.sleep(0.5)

        for i in range(1, 10):
            # 如果第一個不等於已付款，就跳下一個，
            if self.get_text(xpath="//div[@class='card'][2]/div/div/div/div/table/tbody/tr[%d]/td[5]" % (i) ) == "已付款":
                self.click(xpath="//div[@class='card'][2]/div/div/div/div/table/tbody/tr[%d]/td[6]/button"  % (i) )
                break


        self.click(id_="refund_btn")
        PageWait(page.dialog)
        self.click(id_="refund_submit_btn")
        self.click(id_="refund_sure_btn")
        self.assertAlertText("退款建立  成功!")
        self.accept_alert()


    # def test_refund_reversal(self):
    #     # ElementClickInterceptedException: Message: element click intercepted: Element is not clickable at point (494, 914)
    #     # 解決辦法：https://www.itread01.com/p/514946.html
    #     page = ServicePage(seldom.driver)
    #     menubar = ECPage(Seldom.driver)
    #     menubar.refund_manage.click()
    #     menubar.refund_reversal.click()
    #     n = 0
    #
    #     # try:
    #     # 沒看見這個body
    #     # 有這個body但是是空的,如果有的話才做以下操作
    #     PageWait(page.query_body)
    #
    #     # except:
    #     # print("aaaa")
    #     self.click(id_="confirm_cancelrefund")
    #     self.click(xpath="//button[@type='button']")
    #     PageWait(page.dialog)
    #     self.click(id_="cancelrefund_sure_btn")
    #     self.assertAlertText("取消退款建立  成功!")
    #     self.accept_alert()
        # except:
        #     self.sleep(0.5)
        #     n = n + 1
        #     if n>5:
        #         timeout


    # def test_cancel(self):
    #     page = ServicePage(seldom.driver)
    #     menubar = ECPage(Seldom.driver)
    #     menubar.trnas_manage.click()
    #     menubar.cancel_order.click()
    #     self.click(id_="query_btn")
    #     PageWait(page.query_form)
    #     self.click(xpath="//button[@class='btn btn-info btn-rounded']")
    #     self.sleep(0.5)
    #     self.click(id_="do_cancelbill_btn")
    #     PageWait(page.dialog)
    #     self.click(id_="cancelbill_sure_btn")
    #     self.sleep(0.5)
    #     self.assertEqual(self.get_text(id_="cancelbill_showmessage"), "取消帳單 成功!")
    #     self.click(id_="cancelbill_close_btn")