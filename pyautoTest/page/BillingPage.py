from poium import Page, NewPageElement
class BillingPage(Page):
    """billing page"""

    show_message = NewPageElement(id_="show_message")
    copylink = NewPageElement(id_="copylink")
    logo = NewPageElement(xpath="//div[@class='logo']")
    ccno1 = NewPageElement(name="cc1")
    ccno2 = NewPageElement(name="cc2")
    ccno3 = NewPageElement(name="cc3")
    ccno4 = NewPageElement(name="cc4")
    bill_query = NewPageElement(xpath="//ul[@id='sidebarnav']/li[3]/a/i", describe="帳單查詢")
    dialog = NewPageElement(xpath="//div[@role='dialog']")
    query_form = NewPageElement(xpath="//form[@name='listform']")
