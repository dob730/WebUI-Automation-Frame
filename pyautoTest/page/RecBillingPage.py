from poium import Page, NewPageElement


class RecBillingPage(Page):
    """RecBilling page"""

    product_name = NewPageElement(name="productname")
    alert_success = NewPageElement(xpath="//div[@id='success']/h3")
    # menubar
    recbill = NewPageElement(xpath="//ul[@id='sidebarnav']/li[2]/a/i", describe="繳費單管理")
    recbill_batch_create = NewPageElement(xpath="//ul[@id='sidebarnav']/li[2]/ul/li[2]/a", describe="繳費單管理_批次建立")
    recbill_import = NewPageElement(xpath="//ul[@id='sidebarnav']/li[2]/ul/li[3]/a", describe="繳費單管理_匯入建立")
    recbill_query = NewPageElement(xpath="//ul[@id='sidebarnav']/li[2]/ul/li[4]/a", describe="繳費單管理_繳費單查詢")
    recbill_info = NewPageElement(xpath="//ul[@id='sidebarnav']/li[1]/a/i", describe="繳費項目管理")
    recbill_info_create = NewPageElement(xpath="//ul[@id='sidebarnav']/li[1]/ul/li/a", describe="繳費項目管理_建立")
    recbill_info_import = NewPageElement(xpath="//ul[@id='sidebarnav']/li[1]/ul/li[2]/a", describe="繳費項目管理_建立")
    recbill_info_query = NewPageElement(xpath="//ul[@id='sidebarnav']/li[1]/ul/li[3]/a", describe="繳費項目管理_查詢")
    recurrence_create = NewPageElement(xpath="//ul[@id='sidebarnav']/li[3]/ul/li/a", describe="預約建立")
    reservation = NewPageElement(xpath="//ul[@id='sidebarnav']/li[3]/a/i", describe="預約管理")

    query_form = NewPageElement(id_="queryform2", describe="查詢列表")

    query_result = NewPageElement(id_="results", describe="查詢結果")

    querydetail_btn = NewPageElement(id_="querydetail_btn", describe="檢視按鈕")
    show_message = NewPageElement(id_="show_recbillname", describe="確認發送")
    recbillname = NewPageElement(name="recbillname", describe="繳費單名稱")
    recbillinfo_name = NewPageElement(id_="recbillinfo_name", describe="繳費單名稱")
    surecreate_btn = NewPageElement(id_="surecreate_btn", describe="確認要發送鍵")
    boxSee = NewPageElement(id_="boxSee", describe="付款資訊明細")
    refund_submit = NewPageElement(id_="refund_submit_btn", describe="確認退款送出")
    refund_sure = NewPageElement(id_="refund_sure_btn", describe="確認退款鍵")
    cancelrefund = NewPageElement(id_="btn_cancelrefund", describe="確認取消退款送出")

    view_deletemessage = NewPageElement(id_="view_deletemessage", describe="確定刪除鍵")


