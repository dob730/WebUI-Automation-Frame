from poium import Page, NewPageElement
class ServicePage(Page):
    """service page"""

    userid_input = NewPageElement(id_="USERID", describe="帳號")
    pwd_input = NewPageElement(name="PWD", describe="密碼")
    validate_input = NewPageElement(name="validatecode", describe="驗證碼")
    login_button = NewPageElement(class_name="btn", describe="登入鍵")
    big_apple_button = NewPageElement(xpath="(//button[@type='button'])[6]", describe="大蘋果進入鍵")
    yen_store = NewPageElement(xpath="(//button[@type='button'])[7]", describe="顏顏麵包(電商)進入鍵")
    services = NewPageElement(class_name="dropdown-toggle", describe="選擇服務")
    service = NewPageElement(
        xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']", describe="服務下拉列表")
    recbilling = NewPageElement(xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[6]", describe="繳費收款")
    billing = NewPageElement(
        xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[5]", describe="帳單收款")
    donation = NewPageElement(
        xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[last()]", describe="捐款平台")
    dgtpayment = NewPageElement(
        xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[last()-1]", describe="數位產品收款")
    account = NewPageElement(
        xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[1]", describe="我的帳戶")

    ec = NewPageElement(
        xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[6]", describe="電商購物")

    show_message = NewPageElement(id_="show_message", describe="送出鈕的回應訊息顯示資訊")
    # query_form = NewPageElement(xpath="//form[@name='listform']", describe="查詢結果列表")

