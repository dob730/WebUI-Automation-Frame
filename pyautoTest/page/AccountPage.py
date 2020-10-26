from poium import Page, NewPageElement
class AccountPage(Page):
    """account page"""
    account_withdraw = NewPageElement(xpath="//ul[@id='sidebarnav']/li/a", describe="帳戶提領")
    withdraw = NewPageElement(link_text="提領", describe="提領")
    withdraw_cancel = NewPageElement(link_text="取消提領", describe="取消提領")
    dialog1 = NewPageElement(id_="box1")
    dialog2 = NewPageElement(id_="box2")