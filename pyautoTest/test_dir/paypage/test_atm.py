from seldom import data

import seldom


class AtmTest(seldom.TestCase):

    @data([
        ("第一銀行", 'radio-btnb1'),
        ("彰化銀行", 'radio-btnb2'),
        ("國泰世華", 'radio-btnb3'),
        ("永豐銀行", 'radio-btnb4'),
        ("台銀銀行", 'radio-btnb5'),
    ])
    def test_case(self, name, bank):
        """a simple test case """
        self.open("https://sit.1177tech.com.tw/ServiceTester/payment/paypage/testpage.jsp")
        self.select(name="environment", text="Sit")
        self.clear(name="transcode")
        self.type(name="transcode", text="ISBYH62774")
        self.clear(name="merchantnumber")
        self.type(name="merchantnumber", text="118460")
        self.select(name="paymenttype", text="atm")
        self.click(xpath="//input[@type='submit']")
        if self.get_display(xpath="//div[@class='logo']"):
            self.click(xpath="//label[@for='"+bank+"']")
            self.type(id_="useremail", text="aaa@bbb.com")
            self.type(id_="validatecode", text="1111")
            self.click(id_="btn_next")
        if self.get_display(xpath="//div[@class='logo']"):
            self.assertText("Please complete the payment")

    @data([
        ("第一銀行", 'radio-btnb1', '49')
    ])
    def test_amount_toolow(self, name, bank, amount):
        """a simple test case """
        self.open("https://sit.1177tech.com.tw/ServiceTester/payment/paypage/testpage.jsp")
        self.select(name="environment", text="Sit")
        self.clear(name="transcode")
        self.type(name="transcode", text="ISBYH62774")
        self.clear(name="merchantnumber")
        self.type(name="merchantnumber", text="118460")
        self.clear(name="amount")
        self.type(name="amount", text=amount)
        self.select(name="paymenttype", text="atm")
        self.click(xpath="//input[@type='submit']")
        if self.get_display(xpath="//div[@class='logo']"):
            self.click(xpath="//label[@for='"+bank+"']")
            self.type(id_="useremail", text="aaa@bbb.com")
            self.type(id_="validatecode", text="1111")
            self.click(id_="btn_next")
        if self.get_display(xpath="//div[@class='logo']"):
            self.assertText("交易金額過低")

    @data([
        ("第一銀行", 'radio-btnb1', '30001')
    ])
    def test_amount_toohigh(self, name, bank, amount):
        """a simple test case """
        self.open("https://sit.1177tech.com.tw/ServiceTester/payment/paypage/testpage.jsp")
        self.select(name="environment", text="Sit")
        self.clear(name="transcode")
        self.type(name="transcode", text="ISBYH62774")
        self.clear(name="merchantnumber")
        self.type(name="merchantnumber", text="118460")
        self.clear(name="amount")
        self.type(name="amount", text=amount)
        self.select(name="paymenttype", text="atm")
        self.click(xpath="//input[@type='submit']")
        if self.get_display(xpath="//div[@class='logo']"):
            self.click(xpath="//label[@for='"+bank+"']")
            self.type(id_="useremail", text="aaa@bbb.com")
            self.type(id_="validatecode", text="1111")
            self.click(id_="btn_next")
        if self.get_display(xpath="//div[@class='logo']"):
            self.assertText("交易金額過高")