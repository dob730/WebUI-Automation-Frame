from poium import Page, NewPageElement
class ECPage(Page):
    """Ec page"""

    show_message = NewPageElement(id_="show_message")
    refund_manage = NewPageElement(xpath="//ul[@id='sidebarnav']/li[2]/a/i", describe="退款管理")
    refund = NewPageElement(xpath="//ul[@id='sidebarnav']/li[2]/ul/li/a", describe="退款")
    refund_reversal = NewPageElement(xpath="//ul[@id='sidebarnav']/li[2]/ul/li[2]/a", describe="退款取消")
    # query_form = NewPageElement(xpath="//form[@name='listform']")
    trnas_manage = NewPageElement(xpath="//ul[@id='sidebarnav']/li/a/i")
    cancel_order = NewPageElement(link_text="取消訂單")
    cancelrefund = NewPageElement(id_="confirm_cancelrefund")
    query_button = NewPageElement(id_="query_btn", describe="查詢按鈕")
    query_body = NewPageElement(
        xpath="//div[@id='main-wrapper']/div/div/div[3]/div/div/div/form/div[2]/div/div/table/tbody/tr/td",
        describe="查詢結果表身第一筆")
    dialog = NewPageElement(xpath="//div[@role='dialog']", describe="確認對話dialog")