from seldom import data

import seldom



class MmkTest(seldom.TestCase):

    @data([
        ("7-11"),
        ("全家"),
        ("萊爾富"),
    ])
    def test_case(self, name):
        """a simple test case """
        self.open("https://sit.1177tech.com.tw/ServiceTester/payment/paypage/testpage.jsp")
        self.select(name="environment", text="Sit")
        self.clear(name="transcode")
        self.type(name="transcode", text="ISBYH62774")
        self.clear(name="merchantnumber")
        self.type(name="merchantnumber", text="118460")
        self.select(name="paymenttype", text="mmk")
        self.click(xpath="//input[@type='submit']")
        if self.get_display(xpath="//div[@class='logo']"):
            self.type(id_="useremail", text="aaa@bbb.com")
            self.type(id_="validatecode", text="1111")
            self.click(id_="btn_next")
        if self.get_display(xpath="//div[@class='logo']"):
            self.assertText("Please complete the payment")

    @data([
        (1, '49'),
    ])
    def test_amount_toolow(self, name, amount):
        """a simple test case """
        self.open("https://sit.1177tech.com.tw/ServiceTester/payment/paypage/testpage.jsp")
        self.select(name="environment", text="Sit")
        self.clear(name="transcode")
        self.type(name="transcode", text="ISBYH62774")
        self.clear(name="merchantnumber")
        self.type(name="merchantnumber", text="118460")
        self.clear(name="amount")
        self.type(name="amount", text=amount)
        self.select(name="paymenttype", text="mmk")
        self.click(xpath="//input[@type='submit']")
        if self.get_display(xpath="//div[@class='logo']"):
            self.type(id_="useremail", text="aaa@bbb.com")
            self.type(id_="validatecode", text="1111")
            self.click(id_="btn_next")
        if self.get_display(xpath="//div[@class='logo']"):
            self.assertText("交易金額過低")

    @data([
        (1, '30001'),
    ])
    def test_amount_toohigh(self, name, amount):
        """a simple test case """
        self.open("https://sit.1177tech.com.tw/ServiceTester/payment/paypage/testpage.jsp")
        self.select(name="environment", text="Sit")
        self.clear(name="transcode")
        self.type(name="transcode", text="ISBYH62774")
        self.clear(name="merchantnumber")
        self.type(name="merchantnumber", text="118460")
        self.clear(name="amount")
        self.type(name="amount", text=amount)
        self.select(name="paymenttype", text="mmk")
        self.click(xpath="//input[@type='submit']")
        if self.get_display(xpath="//div[@class='logo']"):
            self.type(id_="useremail", text="aaa@bbb.com")
            self.type(id_="validatecode", text="1111")
            self.click(id_="btn_next")
        if self.get_display(xpath="//div[@class='logo']"):
            self.assertText("交易金額過高")



if __name__ == '__main__':
    seldom.main()

