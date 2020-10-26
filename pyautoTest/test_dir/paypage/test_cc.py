from seldom import data, data_class

import seldom


class CreditCardTest(seldom.TestCase):

    @data([
        ("國泰世華", '4682', '3589', '7611', '6102', '03', '30', '057'),
        ("遠東銀行", '5543', '8500', '0588', '1504', '11', '30', '934'),
        ("中國信託", '3560', '7212', '3456', '0031', '12', '30', '000'),
        ("永豐銀行", '4938', '1701', '3000', '0003', '12', '30', '985'),
        ("彰化商業", '5430', '4500', '0000', '1004', '12', '30', '723'),
        ("花旗銀行", '3565', '6612', '3456', '0027', '12', '30', '000'),
    ])
    def test_case(self, name, card1, card2, card3, card4, month, year, cvc):
        """六張卡付費 """
        self.open("https://sit.1177tech.com.tw/ServiceTester/payment/paypage/testpage.jsp")
        self.select(name="environment", text="Sit")
        self.clear(name="transcode")
        self.type(name="transcode", text="HQMOE34264")
        self.clear(name="merchantnumber")
        self.type(name="merchantnumber", text="118511")
        self.select(name="paymenttype", text="creditcard")
        self.click(xpath="//input[@type='submit']")
        if self.get_display(xpath="//div[@class='logo']"):
            self.type(id_="card1", text=card1)
            self.type(id_="card2", text=card2)
            self.type(id_="card3", text=card3)
            self.type(id_="card4", text=card4)
            self.type(id_="cardexp_month", text=month)
            self.type(id_="cardexp_year", text=year)
            self.type(id_="cardcvc2", text=cvc)
            self.type(id_="validatecode", text="1111")
            self.type(id_="useremail", text="aaa@bbb.com")
            self.click(id_="btn_next")
        if self.get_display(xpath="//input[@type='button']"):
            self.type(name="trans_pwd", text="1")
            self.click(xpath="//input[@type='button']")
        self.assertText("rc=0")

    # @data([
    #     ("國泰世華", '49', '4682', '3589', '7611', '6102', '03', '30', '057'),
    # ])
    # def test_amount_toolow(self, name, amount, card1, card2, card3, card4, month, year, cvc):
    #     """交易金額過低"""
    #     self.open("https://sit.1177tech.com.tw/ServiceTester/payment/paypage/testpage.jsp")
    #     self.select(name="environment", text="Sit")
    #     self.clear(name="transcode")
    #     self.type(name="transcode", text="ISBYH62774")
    #     self.clear(name="merchantnumber")
    #     self.type(name="merchantnumber", text="118460")
    #     self.clear(name="amount")
    #     self.type(name="amount", text=amount)
    #     self.select(name="paymenttype", text="creditcard")
    #     self.click(xpath="//input[@type='submit']")
    #     if self.get_display(xpath="//div[@class='logo']"):
    #         self.type(id_="card1", text=card1)
    #         self.type(id_="card2", text=card2)
    #         self.type(id_="card3", text=card3)
    #         self.type(id_="card4", text=card4)
    #         self.type(id_="cardexp_month", text=month)
    #         self.type(id_="cardexp_year", text=year)
    #         self.type(id_="cardcvc2", text=cvc)
    #         self.type(id_="validatecode", text="1111")
    #         self.type(id_="useremail", text="aaa@bbb.com")
    #         self.click(id_="btn_next")
    #     if self.get_display(xpath="//div[@class='logo']"):
    #         self.assertText("交易金額過低")
    #
    # @data([
    #     ("國泰世華", '4682', '3589', '7611', '6102', '03', '30', '057'),
    # ])
    # def test_alert(self, name, card1, card2, card3, card4, month, year, cvc):
    #     """測試信用卡付款的檢核 """
    #     self.open("https://sit.1177tech.com.tw/ServiceTester/payment/paypage/testpage.jsp")
    #     self.select(name="environment", text="Sit")
    #     self.clear(name="transcode")
    #     self.type(name="transcode", text="ISBYH62774")
    #     self.clear(name="merchantnumber")
    #     self.type(name="merchantnumber", text="118460")
    #     self.select(name="paymenttype", text="creditcard")
    #     self.click(xpath="//input[@type='submit']")
    #     if self.get_display(xpath="//div[@class='logo']"):
    #         self.type(id_="card1", text=card1)
    #         self.type(id_="card2", text=card2)
    #         self.type(id_="card3", text=card3)
    #         self.click(id_="btn_next")
    #         self.assertAlertText("請輸入聯絡Email")
    #         self.accept_alert()
    #         self.type(id_="useremail", text="aaa@bbb.com")
    #         self.click(id_="btn_next")
    #         self.assertAlertText("請輸入驗證碼")
    #         self.accept_alert()
    #         self.type(id_="validatecode", text="1111")
    #         self.click(id_="btn_next")
    #         self.assertAlertText("卡號格式錯誤")
    #         self.accept_alert()
    #         self.type(id_="card4", text=card4)
    #         self.click(id_="btn_next")
    #         self.assertAlertText("卡片到期日格式錯誤")
    #         self.accept_alert()
    #         self.type(id_="cardexp_month", text=month)
    #         self.type(id_="cardexp_year", text=year)
    #         self.click(id_="btn_next")
    #         self.assertAlertText("卡片背三碼 CVC或CVV格式錯誤")
    #         self.accept_alert()
    #         self.type(id_="cardcvc2", text=cvc)
    #         self.click(id_="btn_next")
