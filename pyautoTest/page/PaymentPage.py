from poium import Page, NewPageElement


class PaymentPage(Page):
    """payment page"""
    userid_input = NewPageElement(id_="USERID", describe="帳號")
    pwd_input = NewPageElement(name="PWD", describe="密碼")
    validate_input = NewPageElement(name="validatecode")
    login_button = NewPageElement(class_name="btn")
    button = NewPageElement(xpath="(//button[@type='button'])[6]", describe="第六個進入按鈕")
    services = NewPageElement(class_name="dropdown-toggle")
    payment_service = NewPageElement(
        xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[4]")  # 線上收款
    trans_manage = NewPageElement(xpath="//ul[@id='sidebarnav']/li[1]/a/i", describe="交易管理")
    trans_query = NewPageElement(xpath="//ul[@id='sidebarnav']/li[1]/ul/li/a", describe="訂單查詢")
    query_form = NewPageElement(xpath="//form[@name='form_orders_list']")


