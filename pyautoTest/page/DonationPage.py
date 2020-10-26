from poium import Page, NewPageElement


class DonationPage(Page):
    """donation page"""
    userid_input = NewPageElement(id_="USERID", describe="帳號")
    pwd_input = NewPageElement(name="PWD", describe="密碼")
    validate_input = NewPageElement(name="validatecode")
    login_button = NewPageElement(class_name="btn")
    button = NewPageElement(xpath="(//button[@type='button'])[6]", describe="第六個進入按鈕")
    services = NewPageElement(class_name="dropdown-toggle")
    donation = NewPageElement(
        xpath="//div[@class='dropdown-menu dropdown-menu-right animated bounceInDown show']/a[last()]")  # 捐款平台
    donation_project = NewPageElement(xpath="//ul[@id='sidebarnav']/li[1]/a/i")
    project_create = NewPageElement(xpath="//ul[@id='sidebarnav']/li[1]/ul/li/a")
    donation_quick = NewPageElement(xpath="//ul[@id='sidebarnav']/li[2]/a/i")
    donation_query = NewPageElement(xpath="//ul[@id='sidebarnav']/li[5]/a/i", describe="捐款查詢")
    donation_scan = NewPageElement(xpath="//ul[@id='sidebarnav']/li[4]/a/i", describe="掃碼捐款")
    donation_scan_money = NewPageElement(link_text=u"固定金額碼", describe="固定金額碼")
    query_form = NewPageElement(xpath="//form[@name='listform']")

    donation_approvednumber = NewPageElement(name="approvednumber")
    usename_input = NewPageElement(id_="usename_input", describe="捐款用途")
    donation_amount = NewPageElement(id_="donation_amount")
    mobile = NewPageElement(name="send_mobile")
    send = NewPageElement(id_="surecreate_btn")
    show_message = NewPageElement(id_="show_message")
    close_button = NewPageElement(id_="close_btn")
    select = NewPageElement(xpath="//select[@id='validday']")


    amount = NewPageElement(name= "amount")
    name = NewPageElement(id_="name")
    payphone = NewPageElement(id_="payphone")
    email = NewPageElement(id_="email")
    next_button = NewPageElement(xpath="//button[@class='next']")
    cardnumber = NewPageElement(id_="cardnumber")
    cardexpiry = NewPageElement(id_="cardexpiry")
    validatecode = NewPageElement(id_="verification")
    confirm_pay = NewPageElement(xpath="//button[@class='next']")
    cardcvc = NewPageElement(name="back3")
    trans_result = NewPageElement(xpath="//div[@class='result']/h1")
